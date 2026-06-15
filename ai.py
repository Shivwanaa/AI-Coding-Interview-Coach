from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import json
import streamlit as st
load_dotenv()


client = genai.Client(
    api_key=st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")
)

def _generate_json(prompt: str):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    text = response.text.strip()

    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    return json.loads(text)
from prompts import ANALYSIS_PROMPT, INTERVIEW_EVAL_PROMPT

def analyze(problem, solution, explanation):

    prompt = ANALYSIS_PROMPT.format(
        problem=problem,
        solution=solution,
        explanation=explanation
    )

    return _generate_json(prompt)


def evaluate_answer(question, answer):

    prompt = INTERVIEW_EVAL_PROMPT.format(
        question=question,
        answer=answer
    )

    return _generate_json(prompt)

def transcribe_audio(audio_bytes):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            "Transcribe this interview answer. Return only the spoken text.",
            types.Part.from_bytes(
                data=audio_bytes,
                mime_type="audio/wav"
            )
        ]
    )

    return response.text
