import fs from "fs";
import fetch from "node-fetch";
import multer from "multer";
import nextConnect from "next-connect";

const upload = multer({ dest: "/tmp" });

const handler = nextConnect();
handler.use(upload.single("image"));

const HF_API_URL = "https://api-inference.huggingface.co/models/akhaliq/plant-disease-detection-v1";

handler.post(async (req, res) => {
  try {
    const image = fs.readFileSync(req.file.path);
    const response = await fetch(HF_API_URL, {
      method: "POST",
      headers: {
        Authorization: `Bearer ${process.env.HF_API_KEY}`,
        "Content-Type": "application/octet-stream",
      },
      body: image,
    });

    const result = await response.json();
    const prediction = result[0];
    const disease = prediction.label;
    const confidence = (prediction.score * 100).toFixed(2);

    const treatments = {
      "Tomato___Late_blight": {
        solution: "Use copper-based fungicides and remove infected leaves.",
        shop: "Agrovet Kenya, Nairobi",
      },
      "Apple___Black_rot": {
        solution: "Apply Mancozeb and prune affected branches.",
        shop: "FarmChem Supplies, Nakuru",
      },
    };

    const advice = treatments[disease] || {
      solution: "Consult an agricultural expert.",
      shop: "Nearest Agrovet",
    };

    res.status(200).json({
      disease_detected: disease,
      confidence,
      treatment: advice.solution,
      shop: advice.shop,
    });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Image analysis failed" });
  }
});

export const config = {
  api: {
    bodyParser: false,
  },
};

export default handler;
