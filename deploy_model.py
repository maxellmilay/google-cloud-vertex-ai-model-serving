from google.cloud import aiplatform_v1, aiplatform
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "key.json"

PROJECT_ID = "mlops-433612"  
LOCATION = "us-central1"
ENDPOINT_DISPLAY_NAME = 'titanic_survival_model_endpoint'
STORED_MODEL_NAME = 'titanic_survival_classifier'

# Initialize the client
client = aiplatform_v1.EndpointServiceClient(
    client_options={"api_endpoint": f"{LOCATION}-aiplatform.googleapis.com"}
)

# Set the parent (project and location)
parent = f"projects/{PROJECT_ID}/locations/{LOCATION}"

# List all the endpoints in the specified region
endpoints = client.list_endpoints(parent=parent)

ENDPOINT_ID = ''

print("Finding Endpoint...")

# Find endpoint with the same display name
for endpoint in endpoints:
    if endpoint.display_name == ENDPOINT_DISPLAY_NAME:
        ENDPOINT_ID = endpoint.name.split('/')[-1]
        break

print(f"Endpoint ID for {ENDPOINT_DISPLAY_NAME}: {ENDPOINT_ID}")

endpoint = aiplatform.Endpoint(endpoint_name=f"projects/{PROJECT_ID}/locations/{LOCATION}/endpoints/{ENDPOINT_ID}")

print("Finding Model...")

model_client = aiplatform_v1.ModelServiceClient(
    client_options={"api_endpoint": f"{LOCATION}-aiplatform.googleapis.com"}
)

models = model_client.list_models(parent=parent)

MODEL_ID = ''

# Print model details
for model in models:
    if model.display_name == STORED_MODEL_NAME:
        MODEL_ID = model.name.split('/')[-1]

print(f"Model ID for {STORED_MODEL_NAME}: {MODEL_ID}")

aiplatform.init(project=PROJECT_ID, location=LOCATION)

MODEL_NAME = f"projects/{PROJECT_ID}/locations/{LOCATION}/models/{MODEL_ID}"

model = aiplatform.Model(model_name=MODEL_NAME)

print("Deploying Model...")

model.deploy(
    endpoint=endpoint,
    deployed_model_display_name=MODEL_NAME,
    machine_type='n1-highcpu-16',
    min_replica_count=1,
    max_replica_count=1,
    sync=True,
)

model.wait()

print(model.display_name)
print(model.resource_name)
