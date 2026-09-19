import subprocess


OLLAMA_PATH = r"C:\Users\smile\AppData\Local\Programs\Ollama\ollama.exe"
MODEL = "llama3.2"


def ask_llm(failure_data, rag_results):

    print("===== LLM AGENT =====")
    print("Analyzing failure using RAG knowledge...")

    failure_type = failure_data.get("failure_type", "UNKNOWN")
    test_name = failure_data.get("test_name", "UNKNOWN")
    expected = failure_data.get("expected", "UNKNOWN")
    actual = failure_data.get("actual", "UNKNOWN")

    knowledge_text = ""

    for item in rag_results:
        knowledge_text += (
            f"\nPrevious failure: {item['failure_type']}"
            f"\nTest: {item['test_name']}"
            f"\nError: {item['error_message']}"
            f"\nPrevious solution: {item['solution']}\n"
        )

    prompt = f"""
You are an AI assistant for a self-healing CI/CD pipeline.

Analyze this CI/CD failure.

Current failure:
Failure type: {failure_type}
Test: {test_name}
Expected: {expected}
Actual: {actual}

Relevant previous failures retrieved using RAG:
{knowledge_text}

Provide:
1. Root cause
2. Recommended fix
3. Risk level
4. Recommended recovery action

Keep the answer concise and technical.
"""

    result = subprocess.run(
        [
            OLLAMA_PATH,
            "run",
            MODEL,
            prompt
        ],
        capture_output=True,
        text=True,
        encoding="utf-8"
    )

    if result.returncode != 0:
        print("LLM error:")
        print(result.stderr)
        return None

    response = result.stdout.strip()

    print("\n===== LLM ANALYSIS =====")
    print(response)

    return {
        "model": MODEL,
        "analysis": response
    }


if __name__ == "__main__":

    failure_data = {
        "failure_type": "ASSERTION_FAILURE",
        "test_name": "CalculatorTest.testAddition",
        "expected": "10",
        "actual": "5"
    }

    rag_results = [
        {
            "failure_type": "ASSERTION_FAILURE",
            "test_name": "CalculatorTest.testAddition",
            "error_message": "expected: <10> but was: <5>",
            "solution": "Check the Calculator addition implementation and verify that the add method returns the sum of both inputs."
        }
    ]

    ask_llm(failure_data, rag_results)