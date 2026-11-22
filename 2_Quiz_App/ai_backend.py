# =====================================================================
#  PROJECT 3 (ADVANCED LEVEL): AI QUIZ APP - BACKEND
#  Built with : Python + FastAPI + Google Gemini
#  Job        : Asks Gemini to write quiz questions on ANY topic,
#               keeps the answers secret, and checks the user's answers
#  How to run : uvicorn ai_backend:app --reload --port 8001
#  Test it at : http://127.0.0.1:8001/docs
# =====================================================================


# ---------------------------------------------------------------------
#  SECTION 1: IMPORT LIBRARIES
# ---------------------------------------------------------------------
import uuid                                 # makes unique IDs for each quiz
from dotenv import load_dotenv              # reads GEMINI_API_KEY from .env
from fastapi import FastAPI, HTTPException  # HTTPException = send an error back
from pydantic import BaseModel              # describes the shape of data
from google import genai                    # Google's Gemini library


# ---------------------------------------------------------------------
#  SECTION 2: SETUP
# ---------------------------------------------------------------------
load_dotenv()                       # load the API key from .env
client = genai.Client()             # connect to Gemini
MODEL = "gemini-3.5-flash"          # the model that worked in test_gemini.py

app = FastAPI(title="AI Quiz API")

# Memory to store every quiz we create, WITH answers.
# Format: { "quiz id": [list of questions] }
# Note: this is wiped when the server restarts (a database fixes that later).
QUIZZES = {}


# ---------------------------------------------------------------------
#  SECTION 3: DATA SHAPES (pydantic models)
# ---------------------------------------------------------------------

# Shape of ONE question that Gemini must return.
# We give this to Gemini so it replies in clean JSON, not free text.
class QuizQuestion(BaseModel):
    question: str
    options: list[str]      # exactly 4 choices
    answer: str             # must be exactly one of the options
    explanation: str        # one line on why the answer is right


# What the frontend sends to create a quiz
class QuizRequest(BaseModel):
    topic: str
    num_questions: int = 5          # default 5 if not given
    difficulty: str = "medium"      # easy / medium / hard


# What the frontend sends to submit answers
class AnswerSubmission(BaseModel):
    quiz_id: str
    answers: dict[int, str]         # { question number : chosen option }


# ---------------------------------------------------------------------
#  SECTION 4: ASK GEMINI TO WRITE THE QUESTIONS
# ---------------------------------------------------------------------
def generate_questions(topic, num_questions, difficulty):

    # The PROMPT: clear instructions for the AI
    prompt = f"""
    Create {num_questions} multiple-choice quiz questions about: {topic}
    Difficulty: {difficulty}
    Rules:
    - Each question has exactly 4 options.
    - "answer" must be copied EXACTLY from one of the options.
    - Add a one-line "explanation" for the correct answer.
    - Do not repeat questions.
    """

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config={
            # Ask for JSON in the exact shape of a list of QuizQuestion
            "response_mime_type": "application/json",
            "response_schema": list[QuizQuestion],
        },
    )

    # .parsed turns the JSON into a Python list of QuizQuestion objects
    questions = response.parsed

    # Safety check: AI can make mistakes, so keep only valid questions
    valid_questions = []
    for q in questions:
        if len(q.options) == 4 and q.answer in q.options:
            valid_questions.append(q)

    return valid_questions


# ---------------------------------------------------------------------
#  SECTION 5: API ENDPOINTS
# ---------------------------------------------------------------------

# Health check
@app.get("/")
def home():
    return {"message": "AI Quiz API is running!"}


# Create a new quiz on any topic
@app.post("/generate")
def create_quiz(request: QuizRequest):

    # Basic input checks (send a 400 error for bad input)
    if not request.topic.strip():
        raise HTTPException(status_code=400, detail="Topic cannot be empty")
    if not 1 <= request.num_questions <= 10:
        raise HTTPException(status_code=400, detail="Choose between 1 and 10 questions")

    # Call Gemini (wrapped in try/except because internet calls can fail)
    try:
        questions = generate_questions(
            request.topic, request.num_questions, request.difficulty
        )
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"AI error: {error}")

    if not questions:
        raise HTTPException(status_code=500, detail="AI returned no valid questions, try again")

    # Save the full quiz (with answers) under a new unique ID
    quiz_id = str(uuid.uuid4())
    QUIZZES[quiz_id] = questions

    # Send questions WITHOUT answers to the frontend
    questions_for_user = []
    for number, q in enumerate(questions, start=1):
        questions_for_user.append({
            "id": number,
            "question": q.question,
            "options": q.options,
        })

    return {
        "quiz_id": quiz_id,
        "topic": request.topic,
        "questions": questions_for_user,
    }


# Check the answers for a quiz
@app.post("/submit")
def submit_answers(submission: AnswerSubmission):

    # Find the quiz using its ID
    questions = QUIZZES.get(submission.quiz_id)
    if questions is None:
        raise HTTPException(status_code=404, detail="Quiz not found. Please generate a new quiz.")

    score = 0
    results = []

    for number, q in enumerate(questions, start=1):
        user_answer = submission.answers.get(number)
        is_correct = user_answer == q.answer
        if is_correct:
            score += 1

        results.append({
            "id": number,
            "question": q.question,
            "your_answer": user_answer,
            "correct_answer": q.answer,
            "explanation": q.explanation,
            "is_correct": is_correct,
        })

    return {"score": score, "total": len(questions), "results": results}