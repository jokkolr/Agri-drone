from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Hugging Face Inference API (plant disease model)
HF_API_URL = "https://api-inference.huggingface.co/models/nateraw/plant-disease-model"
HF_API_KEY = os.environ.get("HF_API_KEY")  # Set this in Render Environment Variables

def query_huggingface(image_path):
    with open(image_path, "rb") as f:
        headers = {"Authorization": f"Bearer {HF_API_KEY}"}
        response = requests.post(HF_API_URL, headers=headers, files={"file": f})
    return response.json()

@app.route('/')
def home():
    return "AgriDrone Backend is live with Hugging Face AI!"

@app.route('/analyze-single', methods=['POST'])
def analyze_single():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image = request.files['image']
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
    image.save(filepath)

    results = query_huggingface(filepath)

    return jsonify({
        'message': 'AI analysis complete',
        'filename': image.filename,
        'results': results
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
