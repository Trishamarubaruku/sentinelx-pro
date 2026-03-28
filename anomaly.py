import numpy as np
from sklearn.ensemble import IsolationForest

history = []
model = IsolationForest(contamination=0.1)

def detect_anomaly(data):
    global history, model
    
    cpu = data["cpu"]
    memory = data["memory"]
    
    history.append([cpu, memory])
    
    if len(history) < 10:
        return "LEARNING_PHASE"
    
    X = np.array(history)
    model.fit(X)
    
    prediction = model.predict([[cpu, memory]])
    
    if prediction[0] == -1:
        if cpu > 85:
            return "CRITICAL_ANOMALY"
        return "ANOMALY_DETECTED"
    
    return "NORMAL"