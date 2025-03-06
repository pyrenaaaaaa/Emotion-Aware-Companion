RESPONSES = {
    "happy": "Great to hear you're happy! Keep it up!",
    "sad": "I'm here for you. Take a deep breath and let’s talk.",
    "angry": "Try to stay calm. Maybe take a short break.",
    "neutral": "I’m here if you need anything.",
    "stressed": "Let’s try a 5-minute relaxation exercise!"
}

def generate_response(emotion):
    """Generates a response based on the detected emotion."""
    return RESPONSES.get(emotion, "I'm here to listen.")