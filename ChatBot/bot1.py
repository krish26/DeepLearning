# ai_student_chatbot.py

import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3" 


def greet_user():
    """
    Ask user name and greet them.
    """
    name = input("Hi! What's your name? ").strip()

    if not name:
        name = "Student"

    print(f"\nHello, {name}! ")
    print("I'm your AI study assistant (powered locally).")
    print("Ask me anything about studies, coding, or motivation.\n")

    return name


def generate_response(prompt):
    """
    Send prompt to Ollama and get response.
    """
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        return response.json()["response"].strip()

    except requests.exceptions.RequestException:
        return " Error: Make sure Ollama is running."


def build_prompt(user_input, name):
    """
    Create a structured prompt for better responses.
    """
    return f"""
You are a helpful, friendly study assistant chatbot.

User name: {name}

Rules:
- Give short, clear answers
- Be beginner friendly
- Motivate the student
- If coding, explain simply

User: {user_input}
Bot:
"""


def run_chatbot():
    """
    Main chatbot loop.
    """
    name = greet_user()

    while True:
        user_input = input(f"{name}: ")

        if not user_input.strip():
            print("Bot: Please type something ")
            continue

        if user_input.lower() in ["exit", "bye", "quit"]:
            print("Bot: Goodbye! Keep learning ")
            break

        prompt = build_prompt(user_input, name)
        response = generate_response(prompt)

        print(f"Bot: {response}\n")


if __name__ == "__main__":
    run_chatbot()