from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    results = []
    if request.method == "POST":
        query = request.form["query"]
        res = requests.post(
            "http://127.0.0.1:8000/recommend",
            json={"query": query}
        )
        results = res.json()["results"]
    return render_template("index.html", results=results)

app.run(debug=True)
