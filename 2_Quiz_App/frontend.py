# =====================================================================
#  PROJECT 2 (MID LEVEL): QUIZ APP - FRONTEND
#  Built with : Python + Streamlit + requests
#  Job        : Shows the quiz and talks to the FastAPI backend
#  How to run : 1) Backend must be running: uvicorn backend:app --reload
#               2) In a NEW terminal:      streamlit run frontend.py
# =====================================================================


# ---------------------------------------------------------------------
#  SECTION 1: IMPORT LIBRARIES
# ---------------------------------------------------------------------
import streamlit as st      # builds the web page
import requests             # lets Python call an API (like a browser does)


# ---------------------------------------------------------------------
#  SECTION 2: SETTINGS
# ---------------------------------------------------------------------
# The address where our FastAPI backend is running
API_URL = "http://127.0.0.1:8000"


# ---------------------------------------------------------------------
#  SECTION 3: PAGE SETUP AND HEADING
# ---------------------------------------------------------------------
st.set_page_config(page_title="Quiz App", page_icon="🧠")
st.title("🧠 Python Quiz")
st.caption("Frontend: Streamlit • Backend: FastAPI")


# ---------------------------------------------------------------------
#  SECTION 4: GET QUESTIONS FROM THE BACKEND
# ---------------------------------------------------------------------
# try/except catches errors so the app shows a friendly message
# instead of crashing when the backend is not running.
try:
    response = requests.get(f"{API_URL}/questions")   # call GET /questions
    questions = response.json()                        # convert JSON -> Python list
except requests.exceptions.ConnectionError:
    st.error("❌ Cannot reach the backend. Start it with: uvicorn backend:app --reload")
    st.stop()                                          # stop running the page here


# ---------------------------------------------------------------------
#  SECTION 5: SHOW THE QUIZ
# ---------------------------------------------------------------------
# st.form groups all inputs together. The page does not refresh
# after every click; everything is sent only when Submit is pressed.
with st.form("quiz_form"):

    user_answers = {}       # will store { question id : chosen option }

    # enumerate gives a counter (number) along with each question
    for number, q in enumerate(questions, start=1):
        st.subheader(f"Q{number}. {q['question']}")

        # st.radio shows the options as round buttons
        # index=None -> nothing is selected at the start
        # key        -> a unique name Streamlit needs for each widget
        choice = st.radio(
            "Choose one:",
            q["options"],
            index=None,
            key=f"q_{q['id']}",
        )

        # Save the answer only if the user picked something
        if choice is not None:
            user_answers[q["id"]] = choice

    submitted = st.form_submit_button("Submit Quiz")


# ---------------------------------------------------------------------
#  SECTION 6: SEND ANSWERS TO THE BACKEND AND SHOW THE RESULT
# ---------------------------------------------------------------------
if submitted:

    # Warn if some questions were skipped (but still allow submit)
    if len(user_answers) < len(questions):
        st.warning(f"You answered {len(user_answers)} of {len(questions)} questions.")

    # POST sends data. json= converts our Python dict to JSON automatically.
    response = requests.post(f"{API_URL}/submit", json={"answers": user_answers})
    result = response.json()

    score = result["score"]
    total = result["total"]

    # Show the score in big numbers
    st.header("📊 Your Result")
    st.metric("Score", f"{score} / {total}")
    st.progress(score / total)          # a bar from 0% to 100%

    # A message based on how well the user did
    if score == total:
        st.success("🎉 Perfect score! Excellent!")
        st.balloons()                   # fun animation
    elif score >= total / 2:
        st.info("👍 Good job! Keep practising.")
    else:
        st.warning("📚 Keep learning, you'll get there!")

    # Show each question with right / wrong
    st.subheader("Answer Review")
    for r in result["results"]:
        if r["is_correct"]:
            st.write(f"✅ **{r['question']}** — {r['your_answer']}")
        else:
            your = r["your_answer"] or "Not answered"
            st.write(f"❌ **{r['question']}** — You: {your} | Correct: {r['correct_answer']}")