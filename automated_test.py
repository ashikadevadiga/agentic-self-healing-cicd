from agents.predict.predict_agent import predict_failure
from agents.decision.decision_agent import make_decision
from agents.recover.recovery_agent import recover
from agents.verify.verification_agent import verify_recovery

print("\n====================================")
print("      AUTOMATED PIPELINE TEST")
print("====================================")

test_sensor = {
    "timestamp": "2026-10-01T23:55:00",
    "temperature": 95.0,
    "humidity": 70.0,
    "vibration": 3.0,
    "voltage": 243.0,
    "current": 9.0,
    "status": "ABNORMAL"
}

print("\nSTEP 1: PREDICT")

prediction = predict_failure(test_sensor)

print("\nSTEP 2: DECISION")

action = make_decision(
    prediction["risk_level"],
    prediction["failure_type"]
)

print("\nSTEP 3: RECOVERY")

if action == "INITIATE_RECOVERY":
    recovery_result = recover(
        prediction["failure_type"]
    )
else:
    recovery_result = None

print("\nSTEP 4: VERIFICATION")

verification_status = verify_recovery(
    recovery_result
)

print("\n====================================")
print("       AUTOMATED TEST RESULT")
print("====================================")

if verification_status == "VERIFIED":
    print("PIPELINE TEST: PASSED")
    print("CI STATUS     : SUCCESS")
    exit(0)
else:
    print("PIPELINE TEST: FAILED")
    print("CI STATUS     : FAILURE")
    exit(1)
