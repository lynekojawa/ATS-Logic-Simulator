# 🎯 ATS Logic Simulator: Decoding the Hiring Gatekeeper

## Why I Built This
Graduated, eager to start, and... ghosted. Like many, I faced the frustration of sending countless applications into the void of Applicant Tracking Systems (ATS). 
I couldn't help but wonder: *"Is my resume genuinely weak, or am I just not speaking the algorithm's language?"*

Instead of guessing, I decided to reverse-engineer the "Black Box." 
This project is a custom-built, lightweight ATS simulator designed to help candidates align their resumes with Job Descriptions (JD) by analyzing keyword density and matching weights.

## 🛠️ What It Does
*   **Weighted Keyword Analysis:** Calculates a match score based on Jaccard similarity, giving higher priority to keywords that appear frequently in the JD.
*   **Resume/JD Parser:** Extracts text from PDFs and TXT files, sanitizing them for accurate comparison.
*   **Missing Keyword Identification:** Notifies you exactly which high-value keywords you’re missing, so you can optimize your resume for the next application.
*   **Experience Extraction:** Automatically detects "years of experience" requirements and candidate qualifications.

## ⚙️ Architecture & Logic
I focused on creating a clean, modular logic pipeline:
1.  **Sanitization:** Cleaning raw text via Regex (removing legal/fluff terms, stop-words, and noise).
2.  **Normalization:** Custom stemming logic to ensure terms like "analytics" and "analysis" are treated effectively without over-chopping.
3.  **Weighted Scoring:** Using `collections.Counter` to identify keyword density.
4.  **Visualization:** Built with **Streamlit** for a responsive, clean, and intuitive user interface.

## 🚀 Technical Stack
*   **Language:** Python
*   **UI Framework:** Streamlit
*   **Libraries:** `pypdf` (for extraction), `re` (for regex sanitization), `collections` (for frequency mapping)

## 📈 Lessons Learned
*   **Data Engineering Intuition:** Found that "Stop Words" are not universal; they are context-dependent (e.g., legal fluff vs. technical keywords).
*   **Logic over Libraries:** Sometimes building a custom sanitizer is more effective than using a heavy NLP library that might over-stem or miss specific context.
*   **The "Why" Matters:** By building this, I realized that job hunting isn't just about skill; it's about *mapping* your skills to the specific language of the role.

## 🚧 Current Status & Future Roadmap
*   **Status:** MVP completed and functional.
*   **Next Steps:**
    *   Refining the Stemming algorithm to handle edge cases better.
    *   Expanding the "Company-specific Stop-words" dictionary.
    *   Adding support for more document formats.

---
*Built with curiosity, by lynekojawa*