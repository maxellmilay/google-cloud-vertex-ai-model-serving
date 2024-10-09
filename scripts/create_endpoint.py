from google.cloud import aiplatform
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "key.json"

PROJECT_ID = "mlops-433612"
LOCATION = "us-central1"

ENDPOINT_DISPLAY_NAME = 'titanic_survival_model_endpoint'

endpoint = aiplatform.Endpoint.create(
    display_name=ENDPOINT_DISPLAY_NAME,
    project=PROJECT_ID,
    location=LOCATION,
)

print(endpoint.display_name)
print(endpoint.resource_name)
