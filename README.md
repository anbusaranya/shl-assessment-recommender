# shl-assessment-recommender
SHL Assessment Recommender App using Streamlit

Name: Saranya Anbu
Project: SHL Assessment Recommendation
Date: 2025-12-17

1. Project Overview

The goal of this project is to develop a web-based RAG tool that recommends relevant SHL assessments based on a job description or list of required skills.

Objectives:

Help recruiters select relevant assessments quickly.

Assist candidates in identifying suitable assessments.

Provide downloadable results for HR use.

2. Data Collection

SHL assessment catalog data was scraped and stored in Excel (dataset.xlsx), including:

Assessment name

Skills covered

Assessment URL

This dataset serves as the source for recommendations.

3. Application Design

Platform: Streamlit (Python web app)

Components:

User Input:

Job description or comma-separated skills.

Matching Logic:

Compare user input with each assessment.

Compute a relevance score based on keyword matches.

Output:

Display top 5 recommended assessments with links.

Highlight the highest score.

Option to download results as CSV.

4. Implementation Details

Libraries: pandas, Streamlit, io.BytesIO

Scoring Logic:

Convert text to lowercase

Split user input into words

Count matches per assessment → relevance score

Top-K Recommendation:

Sort by score descending

Display top 5 results

5. Evaluation

Verified top assessments for multiple sample job descriptions.

Manually checked relevance scores for correctness.

Downloaded CSV results to ensure proper formatting.

6. Deployment

GitHub: https://github.com/anbusaranya/shl-assessment-recommender

Web App: https://shl-assessment-recommender-9xcadjibffpdihxbm57pxm.streamlit.app/

Process: Code pushed → Streamlit Community Cloud setup → Live web app

7. Future Improvements

Implement semantic embeddings / TF-IDF for better matching.

Convert logic into REST API returning JSON.

Add fields in CSV: skill category, difficulty level.

Include feedback loop to refine recommendations.

Integrate LLM-based RAG for higher accuracy.

8. Summary

Efficiently collected and processed SHL assessment data.

Built a RAG-style matching system with scoring logic.

Developed an interactive web app with CSV download functionality.

Deployed a live, fully functional web application.
