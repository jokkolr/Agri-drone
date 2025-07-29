from flask import Flask, request, jsonify
import os

# --- AI imports ---
import tensorflow as tf
import numpy as np
from PIL import Image
import tensorflow_hub as hub

# --- Load pre-trained AI model ---
MODEL_URL = "https://tfhub.dev/google/imagenet/mobilenet_v2_140_224/classification/5"
model = hub.load(MODEL_URL)

# Example mapping of some class IDs to plant diseases (simplified)
CLASS_LABELS = {
    0: "Healthy Leaf",
    1: "Powdery Mildew",
    2: "Leaf Blight",
    3: "Rust Fungus",
    4: "Bacterial Spot",
    5: "Early Blight",
    6: "Late Blight",
    7: "Mosaic Virus"
}

app = Flask(__name__)

# Create uploads folder if it doesn't exist
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to preprocess image and get prediction
def predict_disease(image_path):
    img = Image.open(image_path).convert("RGB").resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model(img_array)
    predicted_class = np.argmax(predictions)
    confidence = float(np.max(predictions)) * 100
    disease_name = CLASS_LABELS.get(predicted_class, f"Class {predicted_class}")

    return disease_name, confidence

@app.route('/')
def home():
    return "AgriDrone Backend is running!"

# Route for single image analysis
@app.route('/analyze-single', methods=['POST'])
def analyze_single():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image = request.files['image']
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
    image.save(filepath)

    disease_name, confidence = predict_disease(filepath)

    return jsonify({
        'message': 'Image analyzed successfully',
        'filename': image.filename,
        'disease_detected': disease_name,
        'confidence': f"{confidence:.2f}%"
    })

# Route for multiple image analysis
@app.route('/analyze-batch', methods=['POST'])
def analyze_batch():
    if 'images' not in request.files:
        return jsonify({'error': 'No images uploaded'}), 400

    images = request.files.getlist('images')
    results = []

    for img in images:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], img.filename)
        img.save(filepath)

        disease_name, confidence = predict_disease(filepath)

        results.append({
            'filename': img.filename,
            'disease_detected': disease_name,
            'confidence': f"{confidence:.2f}%"
        })

    return jsonify({
        'message': 'Batch analyzed successfully',
        'results': results
    })

if __name__ == '__main__':
    # Use the port Render assigns
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
