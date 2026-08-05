# 🎯 ATS Logic Simulator: Decoding the Hiring Gatekeeper
[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen?style=for-the-badge&logo=appveyor)]
(https://ats-logic-simulator-aws96gdppj2zhy98aohfu3.streamlit.app/)

## Why I Built This
Graduated, eager to start, and ghosted. Like many, I faced the frustration of sending 
countless applications into the void of Applicant Tracking Systems. I couldn't stop 
wondering: is my resume genuinely weak, or am I just not speaking the algorithm's language?

Instead of guessing, I reverse-engineered the black box. This project is a lightweight 
ATS simulator designed to help candidates align their resumes with job descriptions by 
analyzing keyword density and matching weights.

## 🛠️ What It Does
- **Weighted Keyword Analysis:** Calculates a match score based on Jaccard similarity, 
  giving higher priority to keywords that appear frequently in the JD.
- **Hybrid Zone Scoring:** User selects high-signal JD sections — Qualifications, Duties — 
  and the engine scores against those zones specifically, separate from the global match score.
- **Header Detection:** Engine pulls available section headers from the JD automatically. 
  User decides which zones to prioritize.
- **Missing Keyword Identification:** Surfaces exactly which high-value keywords are 
  absent, by zone.
- **Resume/JD Parser:** Extracts text from PDFs and TXT files, sanitized for accurate 
  comparison.
- **Experience Extraction:** Detects years of experience requirements and candidate 
  qualifications automatically.

## ⚙️ Architecture & Logic
1. **Sanitization:** Raw text cleaned via Regex — legal fluff, stop-words, noise removed.
2. **Stemming Engine:** Enhanced stemming logic handling singular/plural variance, 
   including edge cases for `-es` and `-sses` suffixes.
3. **Header Detector:** Pulls section headers from JD. Zone tracker maps content to 
   each header.
4. **Weighted Scoring:** Global score via `collections.Counter` for keyword density. 
   Signal score against user-selected zones.
5. **Visualization:** Streamlit UI — global score panel and zone-specific signal score panel.

## 🚀 Technical Stack
| Layer | Tools |
|---|---|
| Language | Python |
| UI Framework | Streamlit |
| File Parsing | `pypdf` |
| Text Processing | `re`, `collections` |

## 📋 Changelog

### v2.0 — August 2026
- Refactored single-file architecture into three modules: `constants.py`, 
  `scoring_engine.py`, `ui_dashboard.py`
- Enhanced stemming logic — resolved singular/plural matching issues, 
  added `-es` and `-sses` suffix handling
- Added header detector — engine pulls JD section headers automatically
- Added zone tracker — maps content regions to detected headers
- Added hybrid scoring — global overall score retained, signal score added 
  for user-selected high-value zones
- UI updated to display both global and zone-specific scoring panels

### v1.0 — Initial Release
- Weighted keyword analysis via Jaccard similarity
- Resume and JD parser for PDF and TXT
- Missing keyword identification
- Experience extraction
- Streamlit UI

## 📈 Lessons Learned
- Stop words are not universal — they are context-dependent. Legal fluff and 
  technical keywords require different handling.
- Building a custom sanitizer is more effective than a heavy NLP library that 
  over-stems or loses context.
- Job hunting is not just about skill — it is about mapping your skills to the 
  specific language of the role.

## 🚧 Current Status
Deployed. v2.0 update complete.

## 🤝 Project Credits

| Role | Contributor | Responsibility |
|---|---|---|
| **Lead Architect** | lynekojawa (Human) | Core idea, architectural decisions, audit |
| **Logic Orchestrator** | PODO (Gemini) | System design, logic review, code review |
| **Master Planner** | Orion (Gemini) | Strategic planning, phase roadmaps |
| **Code Partner** | Dante (Claude) | Implementation review, debugging |
| **Code Partner** | mini-Dante (Claude) | Code review|

---
*Built with curiosity, by lynekojawa*