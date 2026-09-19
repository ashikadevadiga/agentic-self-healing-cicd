import sys
import os
import time

# Project root
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from iot.iot_sensor import generate_sensor_reading
from agents.monitor.monitor_agent import monitor_ci
from agents.predict.predict_agent import predict_failure
from agents.decision.decision_agent import make_decision
from agents.recover.recover_agent import recover


def run_iot_pipeline():

    print()
    print("================================")
    print(" AGENTIC IOT SELF-HEALING SYSTEM")
    print("================================")

    # --------------------------------
    # 1. GENERATE SENSOR DATA
    # --------------------------------

    print()
    print("[1] IoT SENSOR")

    generate_sensor_reading()

    # Give the file time to be created
    time.sleep(1)

    # --------------------------------
    # 2. MONITOR
    # --------------------------------

    print()
    print("[2] MONITOR AGENT")

    monitor_data = monitor_ci()

    print()
    print("Monitor result:")
    print(monitor_data)

    if monitor_data.get("status") != "FAILURE_DETECTED":

        print()
        print("No sensor failure detected.")
        print("System operating normally.")

        return

    # --------------------------------
    # 3. PREDICT
    # --------------------------------

    print()
    print("[3] PREDICT AGENT")

    prediction_data = predict_failure(monitor_data)

    print()
    print("Prediction result:")
    print(prediction_data)

    # --------------------------------
    # 4. DECISION
    # --------------------------------

    print()
    print("[4] DECISION AGENT")

    decision_data = make_decision(prediction_data)

    print()
    print("Decision result:")
    print(decision_data)

    # --------------------------------
    # 5. RECOVERY
    # --------------------------------

    print()
    print("[5] RECOVERY AGENT")

    recovery_data = recover(decision_data)

    print()
    print("Recovery result:")
    print(recovery_data)

    # --------------------------------
    # 6. FINAL VERIFICATION
    # --------------------------------

    print()
    print("================================")
    print(" FINAL VERIFICATION")
    print("================================")

    print(
        "Recovery status :",
        recovery_data.get("status")
    )

    print(
        "Test result     :",
        recovery_data.get("test_result")
    )

    if recovery_data.get("status") == "RECOVERY_SUCCESS":

        print()
        print("✅ IoT SELF-HEALING SUCCESSFUL")
        print("The sensor failure was automatically recovered.")

    else:

        print()
        print("❌ IoT SELF-HEALING FAILED")
        print("Manual intervention required.")

    print()
    print("================================")
    print(" IOT PIPELINE FINISHED")
    print("================================")


if __name__ == "__main__":
    run_iot_pipeline()