# 🔐 Phishing URL Scanner 🛡️

Welcome to the **Phishing URL Scanner**! This project uses **Python**, **Machine Learning**, and **Flask** to detect phishing URLs. It helps you identify potentially malicious websites by analyzing the URLs using a trained machine learning model.

## 🚀 Features

- **Machine Learning Model**: Classifies URLs as phishing or legitimate.
- **Flask API**: Simple web API to interact with the model.
- **Real-Time Detection**: Make requests and get real-time analysis.
- **Docker Support**: Easily deploy the app using Docker.
- **User-Friendly**: Intuitive and easy-to-use setup for developers and analysts.

## 📋 Table of Contents

- [Installation & Setup](#installation-and-setup)
- [How to Use](#how-to-use)
- [Docker (Optional)](#docker-optional)
- [Model Training (Optional)](#model-training-optional)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## 🛠️ Installation and Setup

To get started with the Phishing URL Scanner, follow the instructions below:

### 1. Clone the Repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/E-debug-dotcom/Phishing-URL-Scanner.git
cd Phishing-URL-Scanner
```
### 2. Set Up the Environment

You can create a virtual environment to isolate the dependencies:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install Dependencies

Once your environment is set up, install the required Python libraries:

```bash
pip install -r requirements.txt
```
### 4. Run the Flask Application

Now that everything is set up, you can run the Flask app:

```bash
python app.py
```

## ⚡ How to Use

### 1. Access the API

To use the Phishing URL Scanner, you can make a POST request to the /predict endpoint.

Example Request : 
```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"url": "http://phishing-site.com"}' \
  http://127.0.0.1:5000/predict
```
