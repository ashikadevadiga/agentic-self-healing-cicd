import json
from datetime import datetime


RECOVERY_LOG = "iot/recovery_log.json"


def recover(failure_type):

    print("\n====================================")
    print("        RECOVERY AGENT")
    print("====================================")

    print(f"Failure detected : {failure_type}")

    if failure_type == "HIGH_TEMPERATURE":
        action = "COOLING_SYSTEM_RESTARTED"

    elif failure_type == "HIGH_VIBRATION":
        action = "MOTOR_RESTARTED"

    elif failure_type == "VOLTAGE_ANOMALY":
        action = "VOLTAGE_CONTROL_RESTARTED"

    elif failure_type == "HIGH_CURRENT":
        action = "CURRENT_CONTROL_RESTARTED"

    elif failure_type == "HIGH_HUMIDITY":
        action = "HUMIDITY_CONTROL_ACTIVATED"

    else:
        action = "NO_RECOVERY_REQUIRED"

    recovery_record = {
        "timestamp": datetime.now().isoformat(),
        "failure_type": failure_type,
        "action": action,
        "status": "RECOVERY_COMPLETED"
    }

    try:
        with open(RECOVERY_LOG, "w") as file:
            json.dump(recovery_record, file, indent=4)

        print(f"Recovery action : {action}")
        print("Recovery status : RECOVERY_COMPLETED")
        print(f"Recovery log saved to: {RECOVERY_LOG}")

    except Exception as e:
        print(f"ERROR saving recovery log: {e}")

    return recovery_record


if __name__ == "__main__":
    print("Recovery Agent ready.")
