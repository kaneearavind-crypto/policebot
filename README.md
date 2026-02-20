# 🚔 Police Command Center AI - Streamlit App

This project is a **Police Command Center AI** web application built with Streamlit and Ollama. It allows officers to interact with an AI-powered assistant for communication, case reporting, and criminal database lookups.

---

## Features

* Interactive officer communication console
* Multiple AI personalities: Professional, Strict Commander, Friendly Patrol Officer
* System modes: Normal Chat, Case Report Mode, Criminal Database Lookup
* Adjustable response randomness (temperature)
* Live chat display with user and AI messages
* Emergency siren activation animation
* Custom background and themed UI for immersive experience

---

## Installation

1. **Clone the repository**:

```bash
git clone https://github.com/yourusername/PoliceCommandCenterAI.git
cd PoliceCommandCenterAI
```

2. **Install dependencies**:

```bash
pip install streamlit ollama
```

---

## Usage

### Run the app

```bash
streamlit run app.py
```

### Sidebar Controls

* **Select AI Model**: Choose your Ollama model (e.g., `gemma3:latest`)
* **Response Randomness**: Adjust the AI response temperature (0.0–1.5)
* **Officer Personality**: Pick the personality style for the AI
* **System Mode**: Choose between Normal Chat, Case Report Mode, or Criminal Database Lookup
* **Activate Siren**: Trigger an emergency siren animation

### Main Panel

* Enter messages in the custom text area
* Use `Send Message` to communicate with the AI
* Use `Clear Chat` to reset the conversation
* Live Communication Feed displays messages from the user and AI with different styles

---

## UI & Styling

* Background image is set via CSS
* Chat messages styled for user (`chat-user`) and AI (`chat-bot`)
* Header box with gradient and gold border
* Emergency siren animation using CSS keyframes

---

## Dependencies

* `streamlit` – for building the web app
* `ollama` – for AI chat functionality

---

## Notes

* Make sure you have access to the Ollama API and proper models configured
* The app is designed to be visually themed for police operations, with custom CSS styling

---

## License

MIT License
