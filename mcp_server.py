"""
mcp_server.py

This FastAPI server exposes EduChain-based tools for use with an MCP client like Claude Desktop.
It provides endpoints to generate multiple-choice questions and lesson plans for educational topics.

Author: [Your Name]
Date: [Assignment Date]
"""

from fastapi import FastAPI
from pydantic import BaseModel
from educhain.generators import QuestionGenerator

app = FastAPI()
qg = QuestionGenerator()

class MCQRequest(BaseModel):
    topic: str
    count: int = 5

class LessonPlanRequest(BaseModel):
    subject: str

@app.post("/generate-mcqs")
async def generate_mcqs(req: MCQRequest):
    """
    Generate multiple-choice questions for a given topic.

    Parameters:
    - topic (str): The topic for which MCQs will be generated.
    - count (int): Number of questions to generate.

    Returns:
    A list of dictionaries, each representing a question with options and answer.
    """
    return {"topic": req.topic, "questions": qg.generate_mcqs(req.topic, req.count)}

@app.post("/lesson-plan")
async def get_lesson_plan(req: LessonPlanRequest):
    """
    Generate a lesson plan outline for a given subject.

    Parameters:
    - subject (str): The subject for the lesson plan.

    Returns:
    A list of lesson topics as a plan.
    """
    return {
        "subject": req.subject,
        "plan": [
            f"Intro to {req.subject}",
            f"Core concepts of {req.subject}",
            f"Activities related to {req.subject}",
            f"Assessment on {req.subject}"
        ]
    }

@app.get("/")
async def root():
    """
    Health check route for the MCP server.
    """
    return {"message": "EduChain MCP server is running 🚀"}
