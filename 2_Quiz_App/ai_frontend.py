# =====================================================================
#  PROJECT 3 (ADVANCED LEVEL): AI QUIZ APP - FRONTEND
#  Built with : Python + Streamlit + requests
#  Job        : Lets the user pick ANY topic, shows the AI quiz,
#               and shows the score with explanations
#  How to run : 1) Backend running: uvicorn ai_backend:app --reload --port 8001
#               2) New terminal:    streamlit run ai_frontend.py
# =====================================================================


# ---------------------------------------------------------------------
#  SECTION 1: IMPORT LIBRARIES
# ---------------------------------------------------------------------
import streamlit as st
import requests


# ---------------------------------------------------------------------
#  SECTION 2: SETTINGS
# ---------------------------------------------------------------------
API_URL = "http://127.0.0.1:8001"     # our AI backend (port 8001)


# ---------------------------------------------------------------------
#  SECTION 3: SESSION STATE (the app's memory)
# ---------------------------------------------------------------------
# IMPORTANT CONCEPT:
# Streamlit re-runs the WHOLE script on every click. Normal variables
# are lost each time. st.session_state is a dictionary that SURVIVES
# re-runs, so we keep the quiz and the result there.
if "quiz" not in st.session_state:
    st.session_state.quiz = None        # the quiz from the backend
if "result" not in st.session_state:
    st.session_state.result = None      # the score after submitting


# ---------------------------------------------------------------------
#  SECTION 4: HELPER FUNCTION TO CALL THE BACKEND
# ---------------------------------------------------------------------
# One function for all POST calls, so error handling is in one place.
# Returns the JSON data, or None if something went wrong.
def call_api(endpoint, data):
    try:
        response = requests.post(f"{API_URL}{endpoint}", json=data, timeout=90)
    except requests.exceptions.ConnectionError:
        st.error("❌ Backend not running. Start it with: uvicorn ai_backend:app --reload --port 8001")
        return None
    except requests.exceptions.Timeout:
        st.error("⏳ The AI took too long. Please try again.")
        return None

    # status_code 200 means success; anything else is an error
    if response.status_code != 200:
        st.error(f"⚠️ {response.json().get('detail', 'Something went wrong')}")
        return None

    return response.json()


# ---------------------------------------------------------------------
#  SECTION 5: PAGE SETUP AND HEADING
# ---------------------------------------------------------------------
st.set_page_config(page_title="AI Quiz", page_icon="🤖")
st.title("🤖 AI Quiz Generator")
st.caption("Any topic • Questions written by Gemini • Backend: FastAPI")


# ---------------------------------------------------------------------
#  SECTION 6: QUIZ SETTINGS (topic, difficulty, number of questions)
# ---------------------------------------------------------------------
st.header("1. Choose Your Topic")

topic = st.text_input("Topic", placeholder="e.g. AI data engineer market trends")

# st.columns puts two widgets side by side
col1, col2 = st.columns(2)
with col1:
    difficulty = st.selectbox("Difficulty", ["easy", "medium", "hard"], index=1)
with col2:
    num_questions = st.slider("Number of questions", min_value=3, max_value=10, value=5)

if st.button("✨ Generate Quiz", type="primary"):
    if not topic.strip():
        st.warning("Please type a topic first.")
    else:
        # st.spinner shows a loading animation while the AI works
        with st.spinner("Gemini is writing your quiz..."):
            quiz = call_api("/generate", {
                "topic": topic,
                "num_questions": num_questions,
                "difficulty": difficulty,
            })
        if quiz:
            st.session_state.quiz = quiz        # save the new quiz
            st.session_state.result = None      # clear any old result


# ---------------------------------------------------------------------
#  SECTION 7: SHOW THE QUIZ
# ---------------------------------------------------------------------
quiz = st.session_state.quiz

if quiz:
    st.header(f"2. Quiz: {quiz['topic']}")

    with st.form("quiz_form"):
        user_answers = {}

        for q in quiz["questions"]:
            st.subheader(f"Q{q['id']}. {q['question']}")
            choice = st.radio(
                "Choose one:",
                q["options"],
                index=None,
                # key includes quiz_id so a NEW quiz starts with empty answers
                key=f"{quiz['quiz_id']}_{q['id']}",
            )
            if choice is not None:
                user_answers[q["id"]] = choice

        submitted = st.form_submit_button("Submit Answers")

    if submitted:
        if len(user_answers) < len(quiz["questions"]):
            st.warning(f"You answered {len(user_answers)} of {len(quiz['questions'])} questions.")

        result = call_api("/submit", {
            "quiz_id": quiz["quiz_id"],
            "answers": user_answers,
        })
        if result:
            st.session_state.result = result


# ---------------------------------------------------------------------
#  SECTION 8: SHOW THE RESULT WITH EXPLANATIONS
# ---------------------------------------------------------------------
result = st.session_state.result

if result:
    score, total = result["score"], result["total"]
    percent = round(score / total * 100)

    st.header("3. Your Result")
    st.metric("Score", f"{score} / {total}", f"{percent}%")
    st.progress(score / total)

    if score == total:
        st.success("🎉 Perfect score!")
        st.balloons()
    elif percent >= 50:
        st.info("👍 Good job! Read the explanations to learn more.")
    else:
        st.warning("📚 Keep learning! The explanations below will help.")

    st.subheader("Answer Review")
    for r in result["results"]:
        icon = "✅" if r["is_correct"] else "❌"
        # st.expander makes a box you can click to open / close
        with st.expander(f"{icon} Q{r['id']}. {r['question']}"):
            st.write(f"**Your answer:** {r['your_answer'] or 'Not answered'}")
            st.write(f"**Correct answer:** {r['correct_answer']}")
            st.info(f"💡 {r['explanation']}")