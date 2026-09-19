import psycopg2
import json


def get_connection():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        database="self_healing_db",
        user="postgres",
        password="Ashika@123"
    )


def save_pipeline_run(
    failure_data,
    prediction_data,
    decision_data,
    recovery_result
):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO pipeline_runs (
            status,
            test_name,
            expected_value,
            actual_value,
            failure_type,
            prediction,
            decision,
            recovery
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    """

    cursor.execute(
        query,
        (
            failure_data["status"],
            failure_data["test"],
            failure_data["expected"],
            failure_data["actual"],
            failure_data["failure_type"],
            json.dumps(prediction_data),
            json.dumps(decision_data),
            json.dumps(recovery_result)
        )
    )

    connection.commit()

    cursor.close()
    connection.close()

    print("Database: Pipeline run saved successfully.")


if __name__ == "__main__":
    try:
        connection = get_connection()
        print("PostgreSQL connection successful!")
        connection.close()
    except Exception as error:
        print("PostgreSQL connection failed:")
        print(error)