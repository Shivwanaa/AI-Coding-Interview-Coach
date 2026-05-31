import streamlit as st
from ai import analyze, evaluate_answer, transcribe_audio
from streamlit_mic_recorder import mic_recorder
from ui import (
    show_analysis,
    show_question,
    show_feedback,
    show_final_score
)
st.set_page_config(
    page_title="AI Coding Interview Coach",
    page_icon="🤖",
    layout="wide"
)
st.title("🤖 AI Coding Interview Coach")
if "analysis" not in st.session_state:
    st.session_state.analysis = None
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
if "scores" not in st.session_state:
    st.session_state.scores = []
if "feedback" not in st.session_state:
    st.session_state.feedback = None
problem = st.text_area(
    "Paste Problem Statement"
)
solution = st.text_area(
    "Paste Your Solution"
)
audio = mic_recorder(
    start_prompt="🎤 Record Explanation",
    stop_prompt="⏹ Stop Recording",
    key="explanation_audio"
)
if audio:
    transcript = transcribe_audio(audio["bytes"])
    st.session_state.explanation = transcript
explanation = st.text_area(
    "Explain your solution as if you're in an interview",
    value=st.session_state.get(
        "explanation",
        ""
    )
)
if st.button("Analyze"):
    if not problem or not solution or not explanation:
        st.error(
            "Please fill all fields."
        )
    else:
        with st.spinner("Analyzing..."):
            st.session_state.analysis = analyze(
                problem,
                solution,
                explanation
            )
            st.session_state.question_index = 0
            st.session_state.scores = []
            st.session_state.feedback = None
analysis = st.session_state.analysis
if analysis:
    show_analysis(analysis)
    questions = analysis["follow_up_questions"]
    idx = st.session_state.question_index
    st.divider()
    if idx >= len(questions):
        if st.session_state.scores:
            show_final_score(
                st.session_state.scores
            )
    else:
        current_question = questions[idx]
        show_question(
            current_question,
            idx,
            len(questions)
        )

        audio = mic_recorder(
            start_prompt="🎤 Record Answer",
            stop_prompt="⏹ Stop Recording",
            key=f"answer_audio_{idx}"
        )
        if audio:
            transcript = transcribe_audio(
                audio["bytes"]
            )
            st.session_state[
                f"answer_{idx}"
            ] = transcript

        answer = st.text_area(
            "Your Answer",
            key=f"answer_{idx}"
)
        if st.button("Submit Answer"):
            if answer.strip():
                with st.spinner(
                    "Evaluating..."
                ):
                    st.session_state.feedback = (
                        evaluate_answer(
                            current_question,
                            answer
                        )
                    )
                    st.session_state.scores.append(
                        st.session_state.feedback["score"]
                    )
            else:
                st.warning(
                    "Please enter an answer."
                )
        if st.session_state.feedback:
            show_feedback(
                st.session_state.feedback
            )
            if st.button(
                "Next Question"
            ):
                st.session_state.question_index += 1
                st.session_state.feedback = None
                st.rerun()