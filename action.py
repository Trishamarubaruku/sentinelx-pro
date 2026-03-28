import os

def take_action(decision):
    if decision == "RESTART_SERVICE":
        print("⚙️ Restarting service...")
        # simulate action
    elif decision == "INVESTIGATE":
        print("🔍 Running diagnostics...")
    else:
        print("✅ No action needed")