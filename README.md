# EduChain MCP Server

This project integrates EduChain with an MCP-compatible server using FastAPI. It exposes two tools:

- Generate MCQs (`/generate-mcqs`)
- Get Lesson Plan (`/lesson-plan`)

## Tools

### 1. Generate MCQs
**Endpoint**: `/generate-mcqs`  
**Method**: POST  
**Input**:
```json
{
  "topic": "Python Loops",
  "count": 3
}



Setup Instructions
✅ Prerequisites
Python 3.11

Virtual environment activated

EduChain installed manually from GitHub

FastAPI and Uvicorn installed

✅ Installation
Clone or download this repository

Install required packages:

bash
Copy
Edit
pip install fastapi uvicorn
Run the server:

bash
Copy
Edit
uvicorn mcp_server:app --reload
Open Swagger UI for testing:
http://127.0.0.1:8000/docs