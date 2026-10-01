from agents.monitor.iot_monitor import monitor_sensor
from agents.predict.predict_agent import predict_failure
from agents.decision.decision_agent import make_decision
from agents.recover.recovery_agent import recover
from agents.verify.verification_agent import verify_recovery

print("\n====================================")
print("   AI IOT SELF-HEALING PIPELINE")
print("====================================")

# STEP 1: MONITOR
print("\nSTEP 1: MONITOR")
sensor_data = monitor_sensor()

# STEP 2: PREDICT
print("\nSTEP 2: PREDICT")
prediction = predict_failure(sensor_data)

# STEP 3: DECISION
print("\nSTEP 3: DECISION")

if prediction:
    action = make_decision(
        prediction["risk_level"],
        prediction["failure_type"]
    )
else:
    action = "NO_ACTION"

# STEP 4: RECOVERY
print("\nSTEP 4: RECOVERY")

if action == "INITIATE_RECOVERY":
    recovery_result = recover(
        prediction["failure_type"]
    )
else:
    print("No recovery required.")
    recovery_result = None

# STEP 5: VERIFICATION
print("\nSTEP 5: VERIFICATION")
verification_status = verify_recovery(recovery_result)

# FINAL RESULT
print("\n====================================")
print("        FINAL PIPELINE RESULT")
print("====================================")

if prediction:
    print(f"Risk Level   : {prediction['risk_level']}")
    print(f"Failure Type : {prediction['failure_type']}")

print(f"Action       : {action}")

if recovery_result:
    print(f"Recovery     : {recovery_result['action']}")
    print(f"Recovery     : {recovery_result['status']}")

print(f"Verification : {verification_status}")

print("====================================")
