from google.cloud import aiplatform_v1
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "key.json"

PROJECT_ID = "mlops-433612"  # @param {type:"string"}
LOCATION = "us-central1"  # @param {type:"string"}
ENDPOINT_DISPLAY_NAME = 'titanic_survival_model_endpoint'

# Initialize the client
client = aiplatform_v1.EndpointServiceClient(
    client_options={"api_endpoint": f"{LOCATION}-aiplatform.googleapis.com"}
)

# Set the parent (project and location)
parent = f"projects/{PROJECT_ID}/locations/{LOCATION}"

# List all the endpoints in the specified region
endpoints = client.list_endpoints(parent=parent)

ENDPOINT_ID = ''

# Find endpoint with the same display name
for endpoint in endpoints:
    if endpoint.display_name == ENDPOINT_DISPLAY_NAME:
        ENDPOINT_ID = endpoint.name.split('/')[-1]
        break

print(f"Endpoint ID for {ENDPOINT_DISPLAY_NAME}: {ENDPOINT_ID}")
