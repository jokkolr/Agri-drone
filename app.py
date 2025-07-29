from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Create uploads folder if it doesn't exist
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return "AgriDrone Backend is running!"

# Route for single image upload
@app.route('/analyze-single', methods=['POST'])
def analyze_single():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
    
    image = request.files['image']
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
    image.save(filepath)
    
    return jsonify({'message': 'Image received successfully', 'filename': image.filename})

# Route for multiple image uploads
@app.route('/analyze-batch', methods=['POST'])
def analyze_batch():
    if 'images' not in request.files:
        return jsonify({'error': 'No images uploaded'}), 400
    
    images = request.files.getlist('images')
    saved_files = []
    
    for img in images:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], img.filename)
        img.save(filepath)
        saved_files.append(img.filename)
    
    return jsonify({'message': 'Batch received successfully', 'files': saved_files})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
