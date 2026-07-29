"""
ui_dashboard.py
Streamlit visualization layer
"""
import streamlit as st
from scoring_engine import extract_resume_text, compute_ats_metrics

def render_dashboard() -> None:
    st.set_page_config(layout="wide", page_title="ATS Visual Commander Dashboard")
    st.title("ATS Visual Commander Dashboard")
    st.write("ATS logic is now visual.")

    topcol1, topcol2, topcol3 = st.columns(3)
    left_JD, right_Resume = st.columns(2)

    with left_JD:
        jd_text = st.text_area("Paste your Job Description here", height=500)
    with right_Resume:
        resume_file = st.file_uploader("Upload your Resume here", type=["pdf", "txt"])
        st.markdown(
            """
            <style>
            [data-testid = "stFileUploader"] section{
                padding: 215px 0;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

    if jd_text and resume_file:
        resume_text = extract_resume_text(resume_file)
        metrics = compute_ats_metrics(jd_text, resume_text)

        match_score = metrics["match_score"]
        years_req = metrics["req_experience"]
        years_candidate = metrics["candidate_experience"]
        exp_delta = years_candidate - years_req

        with topcol1:
            st.metric(label="Match Score", value=f"{match_score:.2f}%")
        with topcol2:
            st.metric(label="Required Experience", value=f"{years_req} yrs")
        with topcol3:
            st.metric(
                label="Candidate Experience",
                value=f"{years_candidate} yrs",
                delta=f"{exp_delta} yrs" if exp_delta != 0 else None
            )

        st.divider()
        st.subheader("Missing Keywords (To boost your score)")

        missing_keywords = metrics["missing_keywords"]
        if missing_keywords:
            cols = st.columns(5)
            for i, word in enumerate(missing_keywords):
                cols[i % 5].info(f"**{word}**")
        else:
            st.success("You've captured all critical keywords! Perfect match! :D")
    else:
        topcol1.metric(label="Match Score", value="0%")
        topcol2.metric(label="Required Experience", value="0 yrs")
        topcol3.metric(label="Candidate Experience", value="0 yrs")


if __name__ == "__main__":
    render_dashboard()