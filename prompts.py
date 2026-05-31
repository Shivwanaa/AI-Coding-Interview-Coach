ANALYSIS_PROMPT = """
You are a Senior Software Engineer interviewer.

Analyze the candidate's solution and explanation.

Evaluate the explanation as if the candidate is answering during a real software engineering interview.

Communication score should be based on:
- Clarity
- Correctness
- Discussion of tradeoffs
- Complexity analysis
- Consideration of edge cases

Return ONLY valid JSON.

Schema:

{{
    "time_complexity": "",
    "space_complexity": "",
    "communication_score": 0,
    "communication_feedback": "",
    "communication_strengths": [],
    "communication_improvements": [],
    "edge_cases": [],
    "optimizations": [],
    "follow_up_questions": [],
    "company_feedback": {{
        "google": "",
        "amazon": "",
        "meta": ""
    }}
}}


Problem:
{problem}

Solution:
{solution}

Explanation:
{explanation}
"""


INTERVIEW_EVAL_PROMPT = """
You are a Senior Software Engineer interviewer.

Question:
{question}

Candidate Answer:
{answer}

Evaluate:

Return ONLY valid JSON:

{{
    "score": 0,
    "feedback": "",
    "strengths": [],
    "improvements": []
}}
"""