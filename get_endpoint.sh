curl -X GET \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    "https://us-central1-aiplatform.googleapis.com/v1/projects/mlops-433612/locations/us-central1/endpoints?filter=display_name=titanic_survival_model_endpoint"