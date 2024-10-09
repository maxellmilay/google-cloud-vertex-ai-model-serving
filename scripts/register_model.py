from google.cloud import aiplatform
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "key.json"

REPOSITORY_NAME = 'custom-training'
MODEL_NAME = 'titanic_survival_classifier'
DESTINATION_BLOB_NAME = 'models'
PROJECT_ID = "mlops-433612"  
LOCATION = "us-central1"
BUCKET_NAME = f'{PROJECT_ID}-{REPOSITORY_NAME}'

PROJECT_ID="mlops-433612"
REPO_NAME='custom-training'
IMAGE_URI=f"us-central1-docker.pkg.dev/{PROJECT_ID}/{REPO_NAME}/vertex-ai-custom-fastapi:latest"

aiplatform.init(project=PROJECT_ID, location=LOCATION)

model_gcs_uri = f'gs://{BUCKET_NAME}/{DESTINATION_BLOB_NAME}'

model = aiplatform.Model.upload(
    display_name=MODEL_NAME,
    serving_container_image_uri=IMAGE_URI,
)

print(f"Model registered with ID: {model.resource_name}")
