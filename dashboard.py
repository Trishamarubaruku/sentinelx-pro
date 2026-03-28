import streamlit as st
import psutil
import time

st.set_page_config(layout="wide")
st.title("🧠 SentinelX Pro - AI Monitoring")

cpu = psutil.cpu_percent()
mem = psutil.virtual_memory().percent

col1, col2, col3 = st.columns(3)

col1.metric("CPU", f"{cpu}%")
col2.metric("Memory", f"{mem}%")

if cpu > 85:
    col3.error("🔥 CRITICAL")
elif cpu > 60:
    col3.warning("⚠️ WARNING")
else:
    col3.success("✅ NORMAL")

st.subheader("Live Graph")
st.line_chart({"CPU": [cpu], "Memory": [mem]})

st.subheader("AI Insight")

if cpu > 85:
    st.error("AI Insight: System overload predicted. Immediate action required.")
elif cpu > 60:
    st.warning("AI Insight: Unusual spike detected.")
else:
    st.success("AI Insight: System stable.")

time.sleep(2)
st.rerun()