import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="SHL Assessment Recommender")
st.title("🔍 SHL Assessment Recommendation Tool")

# --- Load Excel safely ---
file_path = r"C:\Users\Creative Computers\OneDrive\Desktop\shl_project\Gen_AI Dataset.xlsx"

try:
    df = pd.read_excel("dataset.xlsx")
    df.columns = df.columns.str.strip()  # Remove leading/trailing spaces
except FileNotFoundError:
    st.error(f"File not found: {file_path}")
    st.stop()
except PermissionError:
    st.error(f"Permission denied. Make sure '{file_path}' is closed and accessible.")
    st.stop()

# --- User input ---
st.write("Enter Job Description or Skills (comma-separated):")
user_input = st.text_area("")

# --- Recommend assessments ---
if st.button("Recommend Assessments"):
    if user_input.strip() == "":
        st.warning("Please enter job description or skills.")
    else:
        # Split input into individual skills
        user_words = [word.strip().lower() for word in user_input.split(",")]

        # Function to calculate match score
        def match_score(text):
            text = str(text).lower()
            return sum(word in text for word in user_words)

        # Apply match score to dataset
        df["score"] = df["Assessment_url"].apply(match_score)

        # Get top 5 assessments sorted by score
        results = df.sort_values("score", ascending=False).head(5)

        if results["score"].sum() == 0:
            st.info("No matching assessments found. Try different keywords.")
        else:
            st.subheader("✅ Recommended Assessments")

            # Find the highest score
            max_score = results["score"].max()

            for i, row in results.iterrows():
                url = row["Assessment_url"]
                score = row["score"]
                
                # Highlight top score in green
                if score == max_score and score > 0:
                    st.markdown(f"<span style='color:green; font-weight:bold;'>Assessment {i+1} - Relevance Score: {score}</span>  [🔗 Link]({url})", unsafe_allow_html=True)
                else:
                    st.markdown(f"Assessment {i+1} - Relevance Score: {score}  [🔗 Link]({url})")

            # --- Prepare CSV for download ---
            csv_buffer = BytesIO()
            results_to_download = results[["Assessment_url", "score"]]
            results_to_download.to_csv(csv_buffer, index=False)
            csv_buffer.seek(0)

            st.download_button(
                label="📥 Download Recommended Assessments as CSV",
                data=csv_buffer,
                file_name="recommended_assessments.csv",
                mime="text/csv"
            )



