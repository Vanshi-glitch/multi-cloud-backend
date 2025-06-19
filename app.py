from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # ← Enable CORS for all routes

mood_responses = {"happy": {"emoji": "😊", "message": "You're shining! 🌞"},
    "sad": {"emoji": "🥺", "message": "Sending virtual hugs 🤗"},
    "excited": {"emoji": "🥳", "message": "Woohoo! Stay hyped! 🔥"},
    "bored": {"emoji": "😐", "message": "Time to do something fun 🎨"},
    "angry": {"emoji": "😡", "message": "Breathe in... breathe out 🌬️"}
    
}

@app.route('/', methods=['POST'])
def get_mood_response():
    data = request.get_json()
    mood = data.get("mood", "").lower()
    response = mood_responses.get(mood, mood_responses)
    return jsonify(response)

if __name__ == '__main__':
    app.run()
