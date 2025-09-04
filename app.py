from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow requests from frontend (S3)

mood_responses = {
    "happy":   {"emoji": "😄", "message": "That’s awesome! Spread the joy!"},
    "sad":     {"emoji": "😢", "message": "Here’s a hug 🤗 — better days are ahead!"},
    "excited": {"emoji": "🤩", "message": "Woohoo! Keep the energy flowing!"},
    "bored":   {"emoji": "😐", "message": "Why not try something creative today?"},
    "angry":   {"emoji": "😠", "message": "Take a deep breath and sip some chai 🍵"},
}

@app.route("/", methods=["POST"])
def mood_response():
    try:
        data = request.get_json(force=True)  # force parse JSON
        mood = data.get("mood", "").lower()
        response = mood_responses.get(
            mood,
            {"emoji": "❓", "message": "Hmm, that’s a new one!"}
        )
        return jsonify(response)
    except Exception as e:
        return jsonify({"emoji": "⚠️", "message": f"Error: {str(e)}"}), 400

if __name__ == "__main__":
    app.run()
