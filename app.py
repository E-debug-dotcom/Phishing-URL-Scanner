from flask import Flask, request, jsonify
import joblib
import numpy as np

# Load trained model
model = joblib.load("phishing_model.pkl")

app = Flask(__name__)


@app.route('/')
def home():
    return "Flask is running!"


def extract_features(url):
    return np.array([[len(url), 1 if "https" in url else 0, url.count('.')]])


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    url = data.get("url")

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    features = extract_features(url)
    prediction = model.predict(features)[0]

    return jsonify({"url": url, "is_phishing": bool(prediction)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
