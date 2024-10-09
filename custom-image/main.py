# Main FastAPI application code
from fastapi import FastAPI, HTTPException
import os
import numpy as np
import pickle
from google.cloud import storage

# Set environment variable for Google Cloud credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "key.json"

app = FastAPI()

# Initialize Google Cloud Storage client
client = storage.Client()

# Project and storage settings
PROJECT_ID = "mlops-433612"
REPOSITORY_NAME = 'custom-training'
BUCKET_NAME = f'{PROJECT_ID}-{REPOSITORY_NAME}'
DESTINATION_BLOB_NAME = 'models/model.pkl'
model_gcs_uri = f'gs://{BUCKET_NAME}/{DESTINATION_BLOB_NAME}'
LOCAL_MODEL_PATH = '/tmp/model.pkl'

# Load the model from Google Cloud Storage
try:
    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.blob(DESTINATION_BLOB_NAME)
    blob.download_to_filename(LOCAL_MODEL_PATH)
    with open(LOCAL_MODEL_PATH, 'rb') as model_file:
        model = pickle.load(model_file)
    print(f"\n\nModel details: {model}\n\n")

except Exception as e:
    print('Failed to load model')
    raise e

# Get environment variables set by Vertex AI
aip_http_port = os.getenv("AIP_HTTP_PORT", "8080")
aip_health_route = os.getenv("AIP_HEALTH_ROUTE", "/v1/health")
aip_predict_route = os.getenv("AIP_PREDICT_ROUTE", "/v1/predict")

# Health Check Endpoint
@app.get(aip_health_route)
def health_check():
    return {"status": "Healthy"}

# Prediction Endpoint
@app.post(aip_predict_route)
def predict(request: dict):
    try:
        if model is None:
            raise HTTPException(status_code=500, detail="Model is not loaded")
        
        instances = request.get("instances")
        parameters = request.get("parameters", {})
        
        # Convert instances to a NumPy array
        input_data = np.array(instances)
        
        # Perform the prediction
        predictions = model.predict(input_data).tolist()
        
        return {"predictions": predictions}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
