import os
import mlflow
import mlflow.pyfunc
from flask import Flask, request, jsonify

# === Configuration Dagshub ===
os.environ["MLFLOW_TRACKING_USERNAME"] = "Daniellejireh87"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "63953bf087e7f6257e9868bb120e7221a35db822"
os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/Daniellejireh87/my-first-repo.mlflow"

# === ID du run logué sur Dagshub ===
RUN_ID = "9a03add082244d75b2ba62c3a747a3fe"
MODEL_URI = f"runs:/{RUN_ID}/random_forest_model_2"

print(f"Loading model from: {MODEL_URI}")
model = mlflow.pyfunc.load_model(MODEL_URI)

# API Flask simple
app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    inputs = data["inputs"]
    predictions = model.predict(inputs)
    return jsonify(predictions.tolist())

if __name__ == "__main__":
    app.run(port=5001)
