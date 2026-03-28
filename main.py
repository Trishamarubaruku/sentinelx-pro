import time
from agents.monitor import get_system_data, check_website
from agents.anomaly import detect_anomaly
from agents.reasoning import reason
from agents.decision import decide
from agents.action import take_action
from agents.alert import send_alert, send_telegram
from utils.logger import log
from utils.memory import store_event

def run():
    while True:
        print("\n🧠 SentinelX Thinking...\n")

        data = get_system_data()
        web = check_website()

        anomaly = detect_anomaly(data)
        action, explanation = reason(anomaly, data)
        decision = decide(action)

        log(f"DATA: {data}")
        log(f"WEBSITE: {web}")
        log(f"ANOMALY: {anomaly}")
        log(f"DECISION: {decision}")

        confidence = 90

        if anomaly not in ["NORMAL", "LEARNING_PHASE"]:
            message = f"""
🚨 SentinelX Alert
Anomaly: {anomaly}
Decision: {decision}
Confidence: {confidence}%
Reason: {explanation}
            """

            send_alert(message)
            send_telegram(message)
            take_action(decision)
            store_event(message)

        time.sleep(3)

if __name__ == "__main__":
    run()