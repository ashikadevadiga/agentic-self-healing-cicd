import json
import os


FAILURE_FILE = "iot_failure.json"


def monitor_ci():

    print()
    print("===== MONITOR AGENT =====")

    if not os.path.exists(FAILURE_FILE):

        print("No IoT failure detected.")
        
        return {
            "status": "NO_FAILURE",
            "failure_type": "NONE",
            "test_name": "IoT Sensor"
        }

    with open(FAILURE_FILE, "r") as file:
        failure_data = json.load(file)

    failure_type = failure_data.get(
        "failure_type",
        "UNKNOWN"
    )

    temperature = failure_data.get(
        "temperature",
        0
    )

    vibration = failure_data.get(
        "vibration",
        0
    )

    print("IoT failure detected!")
    print("Failure Type :", failure_type)
    print("Temperature  :", temperature)
    print("Vibration    :", vibration)

    return {
        "status": "FAILURE_DETECTED",
        "failure_type": failure_type,
        "test_name": "IoT Sensor",
        "temperature": temperature,
        "vibration": vibration
    }


if __name__ == "__main__":

    result = monitor_ci()

    print()
    print("===== MONITOR RESULT =====")
    print(result)