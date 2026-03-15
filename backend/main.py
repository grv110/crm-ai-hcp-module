from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
from agent import run_agent

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Interaction(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "CRM AI Backend Running"}

@app.post("/chat")
def chat(data: Interaction):
    response = run_agent(data.message)
    return {"response": response}