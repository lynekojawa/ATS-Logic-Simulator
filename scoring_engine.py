"""
scoring_engine.py
Logic handling area sanitization, stemming calibration, and reverse-matching metrics.
"""

import re
from collections import Counter
from typing import List, Set, Tuple, Dict, Any
from pypdf import PdfReader
from constants import STOP_WORDS, STEM_EXCLUSION, WORD_TO_NUM

def sanitize_text(raw_text: str) -> List[str]:
    """Tokenize and applies calibrated suffix-stripping without semantic drift"""
    clean_input = raw_text.lower()
    word_list = re.split(r"[^a-zA-A0-9]+", clean_input)

    stemmed_list: List[str] =[]
    for word in word_list:
        if len(word) <2: continue

        if word in STEM_EXCLUSION:
            stemmed_list.append(word)
        elif word.endswith("ies") and len(word) > 5:
            stemmed_list.append(word[:-3] + "y")
        elif word.endswith("es") and not word.endswith("ses") and len(word) > 4:
            stemmed_list.append(word[:-2])
        elif word.endswith("s") and not word.endswith("ss") and len(word) > 3:
            stemmed_list.append(word[:-1])
        else: stemmed_list.append(word)

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

def compute_ats_metrics(jd_text: str, resume_text: str) -> Dict[str, Any]:
    """Executes reverse-matching scoring logic anchored on Job Description coverage."""
    jd_words = sanitize_text(jd_text)
    jd_counts = Counter(jd_words)
    clean_jd_counts = Counter({k:v for k, v in jd_counts.items() if k not in STOP_WORDS})
    jd_signal = set(clean_jd_counts.keys())

    resume_words = sanitize_text(resume_text)
    resume_signal = set(Counter(resume_words).keys())

    matched_keywords = jd_signal & resume_signal
    missing_keywords = jd_signal - matched_keywords

    total_weight = sum(clean_jd_counts.values())
    match_weight = sum(clean_jd_counts[word] for word in matched_keywords)

    match_score = (match_weight / total_weight) * 100 if jd_signal else 0.0

    high_value_missing = sorted(
        missing_keywords,
        key = lambda x: clean_jd_counts[x],
        reverse=True
    )[:50]

    return {
        "match_score": match_score,
        "req_experience": extract_experience(jd_text),
        "candidate_experience": extract_experience(resume_text),
        "missing_keywords": high_value_missing
    }





