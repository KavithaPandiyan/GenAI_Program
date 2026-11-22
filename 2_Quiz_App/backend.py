# =====================================================================
#  PROJECT 2 (MID LEVEL): QUIZ APP - BACKEND
#  Built with : Python + FastAPI
#  Job        : Stores the questions and (in the next step) checks answers
#  How to run : uvicorn backend:app --reload
#  Test it at : http://127.0.0.1:8000/docs
# =====================================================================


# ---------------------------------------------------------------------
#  SECTION 1: IMPORT LIBRARIES
# ---------------------------------------------------------------------
# FastAPI is used to build an API: a program that other programs
# (like our Streamlit frontend) can talk to over the internet.
from fastapi import FastAPI


# ---------------------------------------------------------------------
#  SECTION 2: CREATE THE APP
# ---------------------------------------------------------------------
# "app" is our API. The command "uvicorn backend:app" means:
#   open the file backend.py and run the variable called app
app = FastAPI(title="Quiz API")


# ---------------------------------------------------------------------
#  SECTION 3: QUESTION BANK
# ---------------------------------------------------------------------
# A LIST of DICTIONARIES. Each dictionary is one question.
#   id      -> unique number for each question
#   question-> the question text
#   options -> the 4 choices
#   answer  -> the correct choice (kept SECRET on the backend)
QUESTIONS = [
    {
        "id": 1,
        "question": "Which keyword is used to create a function in Python?",
        "options": ["func", "def", "function", "create"],
        "answer": "def",
    },
    {
        "id": 2,
        "question": "What is the output of print(2 ** 3)?",
        "options": ["6", "8", "9", "5"],
        "answer": "8",
    },
    {
        "id": 3,
        "question": "Which of these is a Python list?",
        "options": ["(1, 2, 3)", "{1, 2, 3}", "[1, 2, 3]", "<1, 2, 3>"],
        "answer": "[1, 2, 3]",
    },
    {
        "id": 4,
        "question": "Which library did we use to build the web page frontend?",
        "options": ["Django", "Streamlit", "Flask", "React"],
        "answer": "Streamlit",
    },
    {
        "id": 5,
        "question": "What does API stand for?",
        "options": [
            "Application Programming Interface",
            "Advanced Python Integration",
            "Automatic Program Input",
            "Applied Process Index",
        ],
        "answer": "Application Programming Interface",
    },
]


# ---------------------------------------------------------------------
#  SECTION 4: API ENDPOINTS (the "doors" the frontend can knock on)
# ---------------------------------------------------------------------

# Endpoint 1: home page - just to check the server is alive
# @app.get("/") means: when someone visits  http://127.0.0.1:8000/
# run the function below and send back what it returns.
@app.get("/")
def home():
    return {"message": "Quiz API is running!"}


# Endpoint 2: send all questions to the frontend
# IMPORTANT: we REMOVE the answer before sending, otherwise anyone
# could see the answers in the browser. The backend keeps them secret.
@app.get("/questions")
def get_questions():
    questions_without_answers = []

    for q in QUESTIONS:
        questions_without_answers.append({
            "id": q["id"],
            "question": q["question"],
            "options": q["options"],
            # note: no "answer" here!
        })

    return questions_without_answers


# ---------------------------------------------------------------------
#  SECTION 5: CHECK ANSWERS AND GIVE A SCORE
# ---------------------------------------------------------------------
# BaseModel (from pydantic, installed with FastAPI) describes the SHAPE
# of the data the frontend must send. FastAPI checks it automatically.
from pydantic import BaseModel


class AnswerSubmission(BaseModel):
    # A dictionary: { question id : option the user picked }
    # Example: {"1": "def", "2": "8"}
    answers: dict[int, str]


# @app.post is used when the frontend SENDS data to the backend
@app.post("/submit")
def submit_answers(submission: AnswerSubmission):
    score = 0               # number of correct answers
    results = []            # details for each question

    for q in QUESTIONS:
        # .get() returns None if the user skipped this question
        user_answer = submission.answers.get(q["id"])
        is_correct = user_answer == q["answer"]

        if is_correct:
            score += 1

        # Now it is safe to reveal the correct answer
        results.append({
            "id": q["id"],
            "question": q["question"],
            "your_answer": user_answer,
            "correct_answer": q["answer"],
            "is_correct": is_correct,
        })

    return {
        "score": score,
        "total": len(QUESTIONS),
        "results": results,
    }