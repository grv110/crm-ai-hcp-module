# AI CRM HCP Interaction Module

This project is an AI-powered CRM interaction system designed for logging and analyzing healthcare professional (HCP) interactions.

## Features

- Log HCP interactions
- Edit interactions
- Summarize interactions
- Suggest follow-up actions
- Search interaction history
- Sentiment tagging

## Tech Stack

Backend:
- FastAPI
- Python

Frontend:
- React

## Project Structure

backend/
- main.py
- agent.py
- tools.py

frontend/
- React UI

## How to Run

### Backend

cd backend
uvicorn main:app --reload

### Frontend

cd frontend/crm-ui
npm start

## API Endpoint

POST /chat

Example request:

{
"message": "log interaction"
}
