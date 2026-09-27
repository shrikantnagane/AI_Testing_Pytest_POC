import json
from google import genai
from utils.ai_client import AIClient

def LLM_as_Judge_Evaluator(question, context, response):
    judge_prompt = f"""
        You are an AI quality evaluator.
        Question:    {question}
        Reference Context:    {context}
        AI Answer:    {response}
        Evaluate the AI answer.
        Return ONLY valid JSON:
        {{
        "relevance_score": 0.0,
        "groundedness_score": 0.0,
        "hallucination_score": 0.0,
        "reason": "short explanation"
        }}
        Scoring:
        - relevance_score: 0 to 1
        1 = completely relevant
        - groundedness_score: 0 to 1
        1 = fully supported by the context
        - hallucination_score: 0 to 1
        0 = no hallucinations
        1 = severe hallucination
        """
    client = AIClient()
    response = client.send_prompt(judge_prompt, ctx=context)

    return json.loads(response)