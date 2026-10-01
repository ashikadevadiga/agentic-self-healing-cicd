from agents.predict.predict_agent import predict_failure
from agents.decision.decision_agent import make_decision
from agents.recover.recovery_agent import recover


print("\n====================================")
print("      SELF-HEALING FAILURE TEST")
print("====================================")


# Simulated abnormal IoT sensor data
test_sensor = {
    "timestamp": "2026-10-01T23:50:00",
    "temperature": 95.0,
    "humidity": 70.0,
    "vibration": 3.0,
    "voltage": 243.0,
    "current": 9.0,
    "status": "ABNORMAL"
}


# STEP 1: PREDICT
print("\nSTEP 1: PREDICT")
prediction = predict_failure(test_sensor)


# STEP 2: DECISION
print("\nSTEP 2: DECISION")
action = make_decision(
    prediction["risk_level"],
    prediction["failure_type"]
)


# STEP 3: RECOVERY
print("\nSTEP 3: RECOVERY")

if action == "INITIATE_RECOVERY":
    recovery_result = recover(
        prediction["failure_type"]
    )

    print("\nRecovery completed successfully.")
else:
    print("No recovery required.")


print("\n====================================")
print("      SELF-HEALING TEST RESULT")
print("====================================")
print(f"Risk Level   : {prediction['risk_level']}")
print(f"Failure Type : {prediction['failure_type']}")
print(f"Action       : {action}")

if action == "INITIATE_RECOVERY":
    print(f"Recovery     : {recovery_result['action']}")
    print(f"Status       : {recovery_result['status']}")

print("====================================")
