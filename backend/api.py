from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

df = pd.read_excel("dataset.xlsx")

class QueryInput(BaseModel):
    query: str

@app.post("/recommend")
def recommend(data: QueryInput):
    words = data.query.lower().split()

    def score(text):
        return sum(word in str(text).lower() for word in words)

    df["score"] = df["Assessment_url"].apply(score)
    top = df.sort_values("score", ascending=False).head(5)

    return {
        "query": data.query,
        "results": top["Assessment_url"].tolist()
    }

