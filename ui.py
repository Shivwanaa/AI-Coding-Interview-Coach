import streamlit as st


def show_analysis(analysis):

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Communication Score",
            f"{analysis['communication_score']}/10"
        )

    with col2:
        st.metric(
            "Time Complexity",
            analysis["time_complexity"]
        )

    with col3:
        st.metric(
            "Space Complexity",
            analysis["space_complexity"]
        )

    st.subheader("Communication Feedback")

    st.info(
        analysis["communication_feedback"]
    )

    st.subheader("Strengths")

    for strength in analysis["communication_strengths"]:
        st.success(strength)

    st.subheader("Areas to Improve")

    for improvement in analysis["communication_improvements"]:
        st.warning(improvement)

    st.subheader("Missed Edge Cases")

    for edge in analysis["edge_cases"]:
        st.warning(edge)

    st.subheader("Optimizations")

    for item in analysis["optimizations"]:
        st.write("•", item)


def show_question(question, current, total):

    st.header("🎤 Mock Interview")

    st.subheader(
        f"Question {current + 1} of {total}"
    )

    st.write(question)


def show_feedback(feedback):

    st.metric(
        "Question Score",
        f"{feedback['score']}/10"
    )

    st.info(
        feedback["feedback"]
    )

    st.subheader("Strengths")

    for item in feedback["strengths"]:
        st.success(item)

    st.subheader("Improvements")

    for item in feedback["improvements"]:
        st.warning(item)


def show_final_score(scores):

    avg = sum(scores) / len(scores)

    st.success(
        "Interview Complete!"
    )

    st.metric(
        "Final Interview Score",
        f"{avg:.1f}/10"
    )