# GenAI Assessment Recommendation System

This project is a FastAPI-based backend application that recommends suitable SHL assessments based on recruiter or job skill queries.

Tech Stack:
- Python
- FastAPI
- Pandas
- Uvicorn
- OpenPyXL

 Project Structure:
 
- app.py – FastAPI backend logic
- dataset.xlsx – SHL assessment dataset
- requirements.txt – Project dependencies
- README.md – Project documentation

API Endpoint:

#POST /recommend
Accepts a JSON request with job skills and returns relevant SHL assessment links.

#Request Body
json
{
  "query": "java python sql"
}
