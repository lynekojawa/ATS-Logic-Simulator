"""
scoring_engine.py
Logic handling area sanitization, stemming calibration, and reverse-matching metrics.
"""

import re
from collections import Counter
from typing import List, Dict, Any, Optional
from pypdf import PdfReader
from constants import STOP_WORDS, STEM_EXCLUSION, WORD_TO_NUM

#updated 8/3
def sanitize_text(raw_text: str) -> List[str]:
    """Tokenize and applies calibrated suffix-stripping without semantic drift"""
    clean_input = raw_text.lower()
    word_list = re.findall(r'\b[a-z]{2,}\b', clean_input)

    stemmed_list: List[str] =[]

    PROTECTED_SUFFIXES = ("ss", "is", "us", "as", "ce", "le", "me", "re", "de", "te", "ve", "ze", "ge", "pe", "ne", "ke", "fe", "ue")

    for word in word_list:
        if len(word) <2: continue

        if word in STEM_EXCLUSION or len(word) <= 3:
            stemmed_list.append(word)
            continue

        if word.endswith(PROTECTED_SUFFIXES):
            stemmed_list.append(word)
            continue

        if word.endswith("ies") and len(word) > 5:
            stemmed_list.append(word[:-3] + "y")

        elif word.endswith("sses"):
            stemmed_list.append(word[:-2])


        elif word.endswith("es") and len(word) > 4:

            prefix = word[:-2]
            if prefix.endswith(("s", "x", "z", "ch", "sh")):
                stemmed_list.append(prefix)
            else:
                stemmed_list.append(word[:-1])

        elif word.endswith("s") and not word.endswith("ss") and len(word) > 3:
            stemmed_list.append(word[:-1])

        else:
            stemmed_list.append(word)

    return stemmed_list

def extract_experience(text: str) -> int:
    """Parses experience numbers and returns the maximum detected value."""
    processed_text = text.lower()
    for word, digit in WORD_TO_NUM.items():
        processed_text = re.sub(r"\b" + word + r"\b", digit, processed_text)

    exp_pattern = r"(\d+)\+?\s*(?:years?|yrs?)"
    matches = re.findall(exp_pattern, processed_text, re.IGNORECASE)
    return max([int(y) for y in matches]) if matches else 0

def extract_resume_text(resume_file: Any) -> str:
    """Extracts raw strings contents from uploaded PDF or TXT files."""
    if resume_file.name.endswith(".pdf"):
        pdf_reader = PdfReader(resume_file)
        text = ""
        for page in pdf_reader.pages:
            content = page.extract_text()
            if content:
                text += content
        return text
    return resume_file.read().decode("utf-8")

def compute_ats_metrics(jd_text: str, resume_text: str, selected_headers: Optional[List[str]] = None) -> Dict[str, Any]:
    """Executes reverse-matching scoring logic anchored on Job Description coverage."""
    full_jd_words = sanitize_text(jd_text)
    full_clean_counts = Counter(
        {k: v for k, v in Counter(full_jd_words).items() if k not in STOP_WORDS and len(k) >= 4})

    if selected_headers:
        analysis_target_text = extract_signal_content(jd_text, selected_headers)
    else:
        analysis_target_text = jd_text

    signal_jd_words = sanitize_text(analysis_target_text)
    signal_clean_counts = Counter(
        {k: v for k, v in Counter(signal_jd_words).items() if k not in STOP_WORDS and len(k) >= 4})

    resume_signal = set(Counter(sanitize_text(resume_text)).keys())

    def get_score(jd_counts, res_set):
        if not jd_counts: return 0.0
        jd_set = set(jd_counts.keys())
        matched = jd_set & res_set
        return (sum(jd_counts[w] for w in matched) / sum(jd_counts.values())) * 100

    overall_score = get_score(full_clean_counts, resume_signal)
    tactical_score = get_score(signal_clean_counts, resume_signal)

    missing_keywords = sorted(set(signal_clean_counts.keys()) - resume_signal,
                              key=lambda x: signal_clean_counts[x],
                              reverse=True)[:50]

    return {
        "overall_score": overall_score,
        "tactical_score": tactical_score,
        "req_experience": extract_experience(jd_text),
        "candidate_experience": extract_experience(resume_text),
        "missing_keywords": missing_keywords,
        "signal_text": analysis_target_text
    }
#added 7/31
def find_jd_headers(raw_text: str) -> List[str]:
    lines =raw_text.split('\n')
    headers = []

    CORE_ANCHORS = [
        "DUTIES", "RESPONSIBILITIES", "TASKING", "SKILLS", "TECHNICAL SKILLS",
        "QUALIFICATION","QUALIFICATIONS", "REQUIREMENT", "WHAT YOU WILL DO", "WHAT WE OFFER",
        "ABOUT THE JOB", "EXPERIENCE"
    ]

    header_pattern = r"^[A-Z\s]{3,}:?$|^[A-Z][a-z]+(\s[A-Z][a-z]+)*:$"

    for line in lines:
        clean_line = line.strip()
        if not clean_line: continue

        word_count = len(clean_line.split())
        char_count = len(clean_line)
        upper_line = clean_line.upper()

        if any(meta in clean_line for meta in ["Posted:", "Country:", "Location:", "Role Type:"]):
            continue
        is_header = False

        if any(anchor in upper_line for anchor in CORE_ANCHORS):
            if word_count <= 6:
                is_header = True

        if not is_header and re.match(header_pattern, clean_line):
            if word_count <= 6:
                is_header = True

        if is_header and char_count <= 60:
            headers.append(clean_line)

    return headers


def extract_signal_content(raw_text: str, selected_headers: List[str]) -> str:
    if not selected_headers:
        return raw_text

    all_headers = find_jd_headers(raw_text)
    header_positions = []

    for h in all_headers:
        for match in re.finditer(r'(?:^|\n)' +re.escape(h), raw_text):
            start_idx = match.start()
            if raw_text[start_idx] == '\n':
                start_idx += 1
            header_positions.append((start_idx, h))
            break

    header_positions.sort()

    combined_signal = ""

    for target in selected_headers:
        try:
            current_idx = next(i for i, pos in enumerate(header_positions) if pos[1] == target)
            start_pos, _ = header_positions[current_idx]

            if current_idx + 1 < len(header_positions):
                end_pos, _ = header_positions[current_idx +1]
            else:
                end_pos = len(raw_text)

            content = raw_text[start_pos +len(target): end_pos].strip()
            combined_signal += " " + content
        except StopIteration:
            continue
    return combined_signal.strip()
