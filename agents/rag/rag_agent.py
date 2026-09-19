import sys
from pathlib import Path

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

from database.db_manager import get_connection


def retrieve_similar_failure(failure_type, test_name):
    print("===== RAG AGENT =====")
    print("Searching knowledge base...")
    print(f"Failure Type : {failure_type}")
    print(f"Test Name    : {test_name}")

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT
            failure_type,
            test_name,
            error_message,
            solution
        FROM failure_knowledge
        WHERE failure_type = %s
        ORDER BY id DESC
        LIMIT 3;
    """

    cursor.execute(query, (failure_type,))
    results = cursor.fetchall()

    cursor.close()
    connection.close()

    if not results:
        print("No similar failure found.")
        return []

    print("\nSimilar failures found:")

    knowledge = []

    for row in results:
        failure = {
            "failure_type": row[0],
            "test_name": row[1],
            "error_message": row[2],
            "solution": row[3]
        }

        knowledge.append(failure)

        print("--------------------------------")
        print("Failure Type :", row[0])
        print("Test Name    :", row[1])
        print("Error        :", row[2])
        print("Solution     :", row[3])

    print("--------------------------------")

    return knowledge


if __name__ == "__main__":

    retrieve_similar_failure(
        "ASSERTION_FAILURE",
        "CalculatorTest.testAddition"
    )