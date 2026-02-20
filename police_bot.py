import streamlit as st
import ollama
import base64
from datetime import datetime

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="🚔 Police Command Center AI",
    layout="wide",
    page_icon="👮"
)

# -----------------------------
# BACKGROUND IMAGE
# -----------------------------
def set_bg():
    st.markdown("""
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1581091012184-5c3c3f7a6b6d");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    .main-panel {
        background: rgba(10, 25, 47, 0.9);
        padding: 20px;
        border-radius: 15px;
        color: white;
    }

    .header-box {
        background: linear-gradient(90deg, #001f3f, #003366);
        padding: 20px;
        border: 3px solid gold;
        border-radius: 15px;
        text-align: center;
    }

    .chat-user {
        background-color: #1f4068;
        padding: 10px;
        border-radius: 10px;
        margin: 5px 0;
    }

    .chat-bot {
        background-color: #16213e;
        padding: 10px;
        border-left: 5px solid gold;
        border-radius: 10px;
        margin: 5px 0;
    }

    .siren {
        animation: flash 1s infinite;
        font-size: 30px;
    }

    @keyframes flash {
        0% { color: red; }
        50% { color: blue; }
        100% { color: red; }
    }
    </style>
    """, unsafe_allow_html=True)

set_bg()

# -----------------------------
# HEADER
# -----------------------------
st.markdown("""
<div class="header-box">
<h1>🚨 POLICE COMMAND CENTER AI 🚨</h1>
<p>Serve • Protect • Analyze • Report</p>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# SIDEBAR CONTROLS
# -----------------------------
with st.sidebar:
    st.header("⚙️ Control Panel")

    model = st.selectbox("Select AI Model", ["gemma3:latest"])

    temperature = st.slider("Response Randomness",
                            0.0, 1.5, 0.7, 0.1)

    personality = st.radio(
        "Officer Personality",
        ["Professional", "Strict Commander", "Friendly Patrol Officer"]
    )

    mode = st.selectbox(
        "System Mode",
        ["Normal Chat",
         "Case Report Mode",
         "Criminal Database Lookup"]
    )

    if st.button("🚨 Activate Siren"):
        st.markdown("<div class='siren'>🚨🚨🚨 EMERGENCY MODE ACTIVATED 🚨🚨🚨</div>",
                    unsafe_allow_html=True)

# -----------------------------
# SESSION STATE
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# MAIN PANEL
# -----------------------------
st.markdown("<div class='main-panel'>", unsafe_allow_html=True)

st.subheader("📋 Officer Communication Console")

# Custom Text Input Box
user_input = st.text_area("📝 Enter your message:", height=120)

col1, col2 = st.columns([1,1])

send_button = col1.button("📨 Send Message")
clear_button = col2.button("🗑 Clear Chat")

if clear_button:
    st.session_state.messages = []

if send_button and user_input:

    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    system_prompt = f"""
    You are a Police Officer AI.
    Personality: {personality}.
    Mode: {mode}.
    Speak professionally like a law enforcement officer.
    """

    response = ollama.chat(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            *st.session_state.messages
        ],
        options={"temperature": temperature}
    )

    reply = response["message"]["content"]

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

# -----------------------------
# DISPLAY CHAT
# -----------------------------
st.markdown("### 📡 Live Communication Feed")

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(
            f"<div class='chat-user'>🗣 {msg['content']}</div>",
            unsafe_allow_html=True)
    else:
        st.markdown(
            f"<div class='chat-bot'>👮 {msg['content']}</div>",
            unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
