memory = []

def store_event(event):
    memory.append(event)

def get_recent_events():
    return memory[-5:]