# POC Pytest AI Testing

A proof-of-concept project for testing AI-powered application behavior using pytest. The project demonstrates how to call a Gemini-based AI client, pass contextual data, evaluate responses, and validate output quality with automated tests.

## Overview

This project focuses on evaluating whether AI-generated responses are:

- relevant to the user question,
- grounded in the provided context,
- free from hallucination,
- and aligned with expected behavior through automated assertions.

It is designed as a simple testing workflow for AI-based answer generation and evaluation.

## Objectives

- Validate AI-generated responses with pytest
- Test context-aware prompting
- Measure response quality using custom evaluation logic
- Explore LLM-as-a-Judge evaluation patterns
- Build a lightweight AI testing prototype

## Project Structure

```text
POC Pytest AI Testing/
├── .env/                  # Local environment files
├── testData/              # Prompt and test data
├── tests/                 # Pytest test cases
│   └── test_prompt.py     # Main AI response tests
├── utils/                 # Project utility modules
│   ├── ai_client.py       # Google GenAI client wrapper
│   ├── rag_client.py     # Sample retrieval logic
│   ├── evaluator.py      # Rule-based quality evaluator
│   └── evaluator_LLM_as_Judge.py
├── .vscode/               # VS Code workspace settings
├── pytest.ini             # Pytest configuration
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── Readme.text            # Brief project summary
└── .env                   # Local environment variables (if present)
```

## Key Components

### AIClient

The `AIClient` class connects to the Google GenAI API using the `GOOGLE_API_KEY` environment variable and sends a context-aware prompt to the model.

### RAGClient

The `RAGClient` simulates a retrieval step by returning a static context and supporting facts for the given question.

### Evaluator

The `Evaluator` class calculates:

- relevance score,
- groundedness score,
- hallucination score.

### LLM_as_Judge_Evaluator

This module uses an AI model to judge another model’s answer and return structured JSON with evaluation metrics.

## Setup

1. Create a virtual environment (optional but recommended).
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your API key:

```env
GOOGLE_API_KEY=your_api_key_here
```

4. Ensure VS Code is configured to use environment variables from `.env` files in terminal sessions if needed.

## Running Tests

From the project root, run:

```bash
python -m pytest -v -s
```

This executes the test suite and prints AI responses for inspection.

## Example Test Coverage

The project includes tests for:

- simple prompt generation,
- relevance evaluation,
- groundedness and hallucination checks,
- LLM-as-a-judge evaluation output validation.

## Notes

- This is a proof of concept and is intended for learning and experimentation.
- The retrieval logic is intentionally minimal and can be replaced with a real database or vector store.
- API availability and rate limits may affect test execution.

## Status

This project is a starting point for building AI-powered test automation using pytest, retrieval-augmented generation, and model-based quality evaluation.
