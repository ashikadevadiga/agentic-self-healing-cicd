from monitor.monitor_agent import monitor_ci
from predict.predict_agent import predict_failure
from decision.decision_agent import make_decision
from recover.recover_agent import recover_system


def run_pipeline():
    print("\n==============================")
    print(" SELF-HEALING CI/CD PIPELINE")
    print("==============================\n")

    # Agent 1: Monitor
    print("STEP 1: MONITOR")
    monitor_ci()

    # Agent 2: Predict
    print("\nSTEP 2: PREDICT")
    predict_failure()

    # Agent 3: Decision
    print("\nSTEP 3: DECISION")
    action = make_decision(
        risk_level="HIGH",
        failure_type="ASSERTION_FAILURE"
    )

    # Agent 4: Recover
    print("\nSTEP 4: RECOVER")
    recover_system(action)

    print("\n==============================")
    print(" PIPELINE COMPLETED")
    print("==============================")


if __name__ == "__main__":
    run_pipeline()