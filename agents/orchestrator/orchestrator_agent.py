import sys
import os

# ============================================
# ADD PROJECT ROOT TO PYTHON PATH
# ============================================

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


# ============================================
# IMPORT AGENTS
# ============================================

from agents.monitor.monitor_agent import monitor_ci
from agents.predict.predict_agent import predict_failure
from agents.decision.decision_agent import make_decision
from agents.recover.recover_agent import recover


# ============================================
# IOT SELF-HEALING PIPELINE
# ============================================

def run_iot_pipeline():

    print()
    print("================================")
    print(" IOT SELF-HEALING PIPELINE")
    print("================================")

    # ----------------------------------------
    # 1. MONITOR AGENT
    # ----------------------------------------

    print()
    print("[1] MONITOR AGENT")

    monitor_data = monitor_ci()

    print()
    print("Monitor result:")
    print(monitor_data)

    # ----------------------------------------
    # STOP IF NO FAILURE
    # ----------------------------------------

    if monitor_data.get("status") != "FAILURE_DETECTED":

        print()
        print("No IoT failure detected.")
        print()
        print("================================")
        print(" IOT PIPELINE FINISHED")
        print("================================")

        return


    # ----------------------------------------
    # 2. PREDICT AGENT
    # ----------------------------------------

    print()
    print("[2] PREDICT AGENT")

    prediction_data = predict_failure(monitor_data)

    print()
    print("Prediction result:")
    print(prediction_data)


    # ----------------------------------------
    # 3. DECISION AGENT
    # ----------------------------------------

    print()
    print("[3] DECISION AGENT")

    decision_data = make_decision(prediction_data)

    print()
    print("Decision result:")
    print(decision_data)


    # ----------------------------------------
    # 4. RECOVERY AGENT
    # ----------------------------------------

    print()
    print("[4] RECOVERY AGENT")

    recovery_data = recover(decision_data)

    print()
    print("Recovery result:")
    print(recovery_data)


    # ----------------------------------------
    # 5. FINAL VERIFICATION
    # ----------------------------------------

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

    print(
        "Temperature     :",
        recovery_data.get("temperature")
    )

    print(
        "Vibration       :",
        recovery_data.get("vibration")
    )


    # ----------------------------------------
    # SUCCESS / FAILURE
    # ----------------------------------------

    if recovery_data.get("status") == "RECOVERY_SUCCESS":

        print()
        print("================================")
        print(" IOT SELF-HEALING SUCCESSFUL")
        print("================================")

        print()
        print("The IoT sensor failure was")
        print("automatically detected, analyzed,")
        print("decided and recovered.")

    else:

        print()
        print("================================")
        print(" IOT SELF-HEALING FAILED")
        print("================================")

        print()
        print("Manual intervention is required.")


    print()
    print("================================")
    print(" IOT PIPELINE FINISHED")
    print("================================")


# ============================================
# PROGRAM START
# ============================================

if __name__ == "__main__":
    run_iot_pipeline()