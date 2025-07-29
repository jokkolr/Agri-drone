# AgriDrone Health Monitor

**AgriDrone Health Monitor** is a web-based platform designed to help farmers monitor crop health using aerial images captured by drones or satellites. The system processes uploaded images, detects crop stress (disease, drought, pests), and presents insights through interactive visualizations and reports.

---

## Features
- **Modern, Mobile-Friendly Web App** – Runs smoothly on phones and computers.
- **Drone Image Upload** – Farmers can easily upload high-resolution farm photos.
- **AI Health Analysis (Planned)** – Detects crop stress, diseases, and water issues using computer vision and NDVI techniques.
- **Visual Health Map (Demo Version)** – Simulates AI analysis by applying red/green overlays for problem areas.
- **Interactive Dashboard (Coming Soon)** – Summarizes field health with charts, statistics, and recommendations.
- **Notifications (Future)** – Farmers get alerts via SMS or email for early problem detection.

---

## How It Works
1. **Drone Image Capture** – A drone flies over a farm and captures high-quality images (RGB or multispectral).  
2. **Upload** – The farmer uploads these images into the AgriDrone web app.  
3. **AI Processing** *(future)* – The system analyzes plant health using machine learning models and NDVI calculations.  
4. **Results** – Displays a visual health map, percentage of stressed crops, and recommended actions.  
5. **Alerts** *(future)* – Sends notifications if issues are detected, so farmers can act quickly.

---

## Tech Stack
- **Frontend:** HTML, CSS (Glassmorphism + 3D animations), Vanilla JavaScript  
- **Backend (Planned):** Node.js & Express (for API and AI integration)  
- **AI/Processing (Planned):** Python (TensorFlow/Keras for plant health detection)  
- **Deployment:** Mobile-first web app, can be hosted on Netlify or Vercel for quick access  

---

## Current Status
- **Phase 1 (Completed):**  
  - Landing page with professional design  
  - Drone image upload and live preview  
  - Interactive UI with animations and plant-themed background  
- **Phase 2 (In Progress):**  
  - Fake NDVI effect to simulate analysis  
  - Results dashboard with charts  
- **Phase 3 (Planned):**  
  - Real AI models for crop health detection  
  - User accounts, alerts, and automated reporting

---

## How to Run
1. Download or clone the repository.
2. Open the `index.html` file in any browser (works on phone and PC).
3. Upload a sample farm image to test the preview.
4. (Coming Soon) Click **Analyze** to simulate crop health detection.

---

## Future Roadmap
- Real AI-driven analysis (NDVI + CNN models).
- Mobile app version (React Native or Flutter).
- Drone integration for **real-time** monitoring.

---

### License
This project is open-source (MIT) – free for personal or commercial use.

---
