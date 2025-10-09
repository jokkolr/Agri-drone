import express from "express";
import multer from "multer";
import fetch from "node-fetch";
import dotenv from "dotenv";

dotenv.config();
const app = express();
const upload = multer({ storage: multer.memoryStorage() });

const HF_TOKEN = process.env.HUGGINGFACE_TOKEN;

app.post("/analyze-single", upload.single("image"), async (req, res) => {
  try {
    const response = await fetch(
      "https://api-inference.huggingface.co/models/plant-disease-classification",
      {
        method: "POST",
        headers: { Authorization: `Bearer ${HF_TOKEN}` },
        body: req.file.buffer,
      }
    );

    const result = await response.json();
    res.json({
      disease_detected: result[0]?.label || "Unknown disease",
      confidence: result[0]?.score ? (result[0].score * 100).toFixed(1) : 0,
    });
  } catch (err) {
    res.status(500).json({ error: "Failed to analyze image" });
  }
});

app.listen(3000, () => console.log("Server running on port 3000"));
