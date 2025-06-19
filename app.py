from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow requests from all origins (including AWS S3 frontend)

# Mood responses dictionary
mood_responses = {
    "happy": {
        "emoji": "😊",
        "message": "You're shining! 🌞"
    },
    "sad": {
        "emoji": "🥺",
        "message": "Sending virtual hugs 🤗"
    },
    "excited": {
        "emoji": "🥳",
        "message": "Woohoo! Stay hyped! 🔥"
    },
    "bored": {
        "emoji": "😐",
        "message": "Time to do something fun 🎨"
    },
    "angry": {
        "emoji": "😡",
        "message": "Breathe in... breathe out 🌬️"
    }
}

# POST route at "/"
@app.route("/", methods=["POST"])
def get_mood_response():
    data = request.get_json()

    # Validate incoming data
    if not data or "mood" not in data:
        return jsonify({
            "emoji": "❌",
            "message": "No mood provided in request."
        }), 400

    # Normalize the mood value
    mood = data.get("mood", "").strip().lower()

    # Get response or default
    response = mood_responses.get(
        mood,
        {"emoji": "❓", "message": "Hmm, never heard of that mood!"}
    )

    return jsonify(response)

# Run locally (not needed on Azure)
if __name__ == "__main__":
    app.run()
