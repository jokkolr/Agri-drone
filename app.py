from flask import Flask, jsonify
import os
from dotenv import load_dotenv

# Load the Hugging Face API key from .env
load_dotenv()
HF_API_KEY = os.environ.get("HF_API_KEY")

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "AgriDrone AI backend is running!",
        "hugging_face_key_loaded": bool(HF_API_KEY)  # Check if key is working
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
