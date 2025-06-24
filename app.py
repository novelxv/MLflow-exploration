from flask import Flask, request, jsonify
import mlflow
import mlflow.sklearn
import pandas as pd

mlflow.set_tracking_uri("http://127.0.0.1:8080")

RUN_ID = "790e4965409d4ae588f296033d856875"
ARTIFACT_PATH = "rf_apples"

model_uri = f"runs:/{RUN_ID}/{ARTIFACT_PATH}"

# Load model from MLflow
model = mlflow.sklearn.load_model(model_uri)

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    df = pd.DataFrame(data)
    
    preds = model.predict(df)
    
    return jsonify({"predictions": preds.tolist()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
