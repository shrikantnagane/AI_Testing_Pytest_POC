
from utils import rag_client
from utils.ai_client import AIClient
from utils.evaluator import Evaluator
from utils.rag_client import RAGClient
from utils.evaluator_LLM_as_Judge import LLM_as_Judge_Evaluator

def test_send_prompt():

    client = AIClient()
    rag_client = RAGClient()
    context, facts = rag_client.retrieve("What is regression testing?")

    response = client.send_prompt(
        "What is regression testing?", ctx=context
    )

    print("\nAI Response:")
    print(response)

    assert response is not None
    assert isinstance(response, str)
    assert len(response) > 0
    assert "regression testing" in response.lower()

def test_relevance_score():

    client = AIClient()
    rag_client = RAGClient()
    context, facts = rag_client.retrieve("What is regression testing?")
    response = client.send_prompt(
        "What is regression testing?", ctx=context
    )

    evaluator = Evaluator()

    relevance_score = evaluator.calculate_relevance(
    "What is regression testing?",
    response
    )

    print(relevance_score)
    assert relevance_score > 0.75

def test_groundedness_and_hallucination():

    rag_client = RAGClient()
    context, facts = rag_client.retrieve("What is regression testing?")

    client = AIClient()
    
    response = client.send_prompt(
            "What is regression testing?", ctx=context  
        )
    
    evaluator = Evaluator()
    groundedness_score = evaluator.calculate_groundedness(response,context,facts
    )

    hallucination_score = evaluator.calculate_hallucination(response,context,facts
    )

    print("Groundedness:", groundedness_score)
    print("Hallucination:", hallucination_score)

    assert groundedness_score >= 0.90
    assert hallucination_score <= 0.1

def test_LLM_as_Judge_Evaluator():

    rag_client = RAGClient()
    context, facts = rag_client.retrieve("What is regression testing?")

    client = AIClient()
    
    response = client.send_prompt(
            "What is regression testing?", ctx=context  
        )
    

    evaluation_result = LLM_as_Judge_Evaluator(
        question="What is regression testing?",
        context=context,
        response=response
    )

    print("Evaluation Result:", evaluation_result)

    assert "relevance_score" in evaluation_result
    assert "groundedness_score" in evaluation_result
    assert "hallucination_score" in evaluation_result
    assert "reason" in evaluation_result