from google.cloud import aiplatform_v1
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "key.json"

PROJECT_ID = "mlops-433612"  # @param {type:"string"}
LOCATION = "us-central1"  # @param {type:"string"}

parent = f"projects/{PROJECT_ID}/locations/{LOCATION}"

model_client = aiplatform_v1.ModelServiceClient(
    client_options={"api_endpoint": f"{LOCATION}-aiplatform.googleapis.com"}
)

models = model_client.list_models(parent=parent)

# Print model list
for model in models:
    print(model.display_name)
