PROJECT_ID="mlops-433612"
REPO_NAME='custom-training'
IMAGE_URI=us-central1-docker.pkg.dev/$PROJECT_ID/$REPO_NAME/vertex-ai-custom-fastapi:latest

docker build -t vertex-ai-custom-fastapi .

docker run -p 8080:8080 vertex-ai-custom-fastapi
