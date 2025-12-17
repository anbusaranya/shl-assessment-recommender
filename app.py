import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="SHL Assessment Recommender")
st.title("🔍 SHL Assessment Recommendation Tool")

# --- Load Excel (Cloud-safe) ---
try:
    df = pd.read_excel("dataset.xlsx")
    df.columns = df.columns.str.strip()
except Exception as e:
    st.error("Dataset file not found or failed to load.")
    st.stop()

# --- User input ---
st.write("Enter Job Description or Skills (comma-separated):")
user_input = st.text_area("")

# --- Recommend assessments ---
if st.button("Recommend Assessments"):
    if user_input.strip() == "":
        st.warning("Please enter job description or skills.")
    else:
        user_words = [word.strip().lower() for word in user_input.split(",")]

        def match_score(text):
            text = str(text).lower()
            return sum(word in text for word in user_words)

        df["score"] = df["Assessment_url"].apply(match_score)
        results = df.sort_values("score", ascending=False).head(5)

        if results["score"].sum() == 0:
            st.info("No matching assessments found. Try different keywords.")
        else:
            st.subheader("✅ Recommended Assessments")

            max_score = results["score"].max()

            for idx, row in results.iterrows():
                url = row["Assessment_url"]
                score = row["score"]

                if score == max_score and score > 0:
                    st.markdown(
                        f"<span style='color:green; font-weight:bold;'>Relevance Score: {score}</span>  [🔗 Link]({url})",
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(f"Relevance Score: {score}  [🔗 Link]({url})")

            # --- CSV Download ---
            csv_buffer = BytesIO()
            results[["Assessment_url", "score"]].to_csv(csv_buffer, index=False)
            csv_buffer.seek(0)

            st.download_button(
                label="📥 Download Results as CSV",
                data=csv_buffer,
                file_name="recommended_assessments.csv",
                mime="text/csv"
            )




