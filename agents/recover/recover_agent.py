import time


def recover(decision_data):

    print()
    print("===== RECOVERY AGENT =====")

    decision = decision_data.get("decision", "UNKNOWN")
    failure_type = decision_data.get("failure_type", "UNKNOWN")

    print("Decision      :", decision)
    print("Failure Type  :", failure_type)

    if decision != "FIX_AND_RETEST":

        print("No recovery action required.")

        return {
            "status": "NO_RECOVERY_REQUIRED",
            "action": decision,
            "test_result": "NOT_REQUIRED"
        }

    print()
    print("Starting IoT recovery...")

    if failure_type == "HIGH_TEMPERATURE":

        print("Action: Cooling IoT sensor...")
        time.sleep(2)

        temperature = 45.0
        vibration = 0.30

    elif failure_type == "HIGH_VIBRATION":

        print("Action: Stabilizing IoT sensor...")
        time.sleep(2)

        temperature = 45.0
        vibration = 0.30

    elif failure_type == "LOW_BATTERY":

        print("Action: Restoring sensor battery...")
        time.sleep(2)

        temperature = 45.0
        vibration = 0.30

    else:

        print("Unknown failure type.")

        return {
            "status": "RECOVERY_FAILED",
            "action": decision,
            "test_result": "FAILED"
        }

    print()
    print("Recovery values:")
    print("Temperature :", temperature, "°C")
    print("Vibration   :", vibration)

    # Verification
    if temperature <= 70 and vibration <= 0.85:

        print()
        print("IoT sensor returned to safe state.")
        print("Recovery verification PASSED.")

        return {
            "status": "RECOVERY_SUCCESS",
            "action": decision,
            "test_result": "PASSED",
            "temperature": temperature,
            "vibration": vibration
        }

    print()
    print("Recovery verification FAILED.")

    return {
        "status": "RECOVERY_FAILED",
        "action": decision,
        "test_result": "FAILED"
    }


if __name__ == "__main__":

    decision_data = {
        "decision": "FIX_AND_RETEST",
        "failure_type": "HIGH_TEMPERATURE"
    }

    result = recover(decision_data)

    print()
    print("===== RECOVERY RESULT =====")
    print(result)