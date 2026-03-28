import psutil
import requests
import time

def get_system_data():
    return {
        "cpu": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent
    }

def check_website(url="https://google.com"):
    try:
        start = time.time()
        response = requests.get(url, timeout=3)
        latency = time.time() - start
        return {
            "status": response.status_code,
            "latency": latency
        }
    except:
        return {"status": "DOWN", "latency": None}