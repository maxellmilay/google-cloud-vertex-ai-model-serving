# Step 1: Base image from Python 3.9 to support FastAPI
FROM python:3.12-slim

# Step 2: Set up working directory
WORKDIR /app

# Step 3: Copy the FastAPI and dependencies configuration
COPY requirements.txt requirements.txt

# Step 4: Install necessary Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy all the application files
COPY . /app

# Step 6: Expose the port required for the FastAPI application
EXPOSE 8080

# Step 7: Set environment variables for Vertex AI
ENV AIP_HTTP_PORT=8080

# Step 8: Define the command to run the FastAPI application
ENTRYPOINT [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080" ]
