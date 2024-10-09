# Custom Vertex AI Serving Container
This project provides a custom container to serve models using FastAPI for Vertex AI.

### Requirements
- Docker
- Vertex AI

### Steps to Use
1. Build the Docker container image:
   ```
   docker build -t vertex-ai-custom-fastapi .
   ```
2. Push the image to Artifact Registry:
   ```
   docker tag vertex-ai-custom-fastapi us-central1-docker.pkg.dev/YOUR_PROJECT/YOUR_REPO/vertex-ai-custom-fastapi:latest
   docker push us-central1-docker.pkg.dev/YOUR_PROJECT/YOUR_REPO/vertex-ai-custom-fastapi:latest
   ```
3. Deploy the container to Vertex AI following the deployment steps.

4. Ensure that the model artifact (`model.pkl`) is uploaded to the specified Cloud Storage bucket.
