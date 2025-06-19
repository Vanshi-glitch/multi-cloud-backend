from flask import Flask, request, jsonify

app = Flask(__name__)

mood_responses = {
    "happy": {"emoji": "😄", "message": "That’s awesome! Spread the joy!"},
    "sad": {"emoji": "😢", "message": "Here’s a hug 🤗 — better days are ahead!"},
    "excited": {"emoji": "🤩", "message": "Woohoo! Keep the energy flowing!"},
    "bored": {"emoji": "😐", "message": "Why not try something creative today?"},
    "angry": {"emoji": "😠", "message": "Take a deep breath and sip some chai 🍵"}
}

@app.route('/', methods=['POST'])
def get_mood_response():
    data = request.get_json()
    mood = data.get("mood", "").lower()
    response = mood_responses.get(mood, {"emoji": "❓", "message": "Hmm, that’s a new one!"})
    return jsonify(response)

if __name__ == "__main__":
    app.run()
