from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api')
def hello():
    return jsonify({"message": "Hello from Azure!"})

if __name__ == '__main__':
    app.run()
