
# Setting Up Minikube on Windows and Running a Flask Docker Application

This guide provides step-by-step instructions to install Minikube on a local Windows machine and deploy a Flask Docker application.

## 1. Install Prerequisites

### a. Install Docker Desktop

1. Download Docker Desktop for Windows from [Docker's official site](https://www.docker.com/products/docker-desktop).
2. Run the installer and follow the prompts.
3. Once installed, launch Docker Desktop and ensure it's running properly.

### b. Install Minikube

1. Download the Minikube executable from the [Minikube releases page](https://github.com/kubernetes/minikube/releases).
   - Look for the latest Windows release and download the `.exe` file.
2. Add Minikube to your system’s PATH:
   - Move the `minikube.exe` file to a directory that's in your PATH (e.g., `C:\Program Files\` or `C:\Windows\System32\`).

### c. Install kubectl

1. Download the `kubectl` binary from the [Kubernetes releases page](https://kubernetes.io/docs/tasks/tools/install-kubectl/).
2. Add `kubectl` to your system’s PATH, similar to Minikube.

## 2. Start Minikube

1. Open a command prompt or PowerShell.
2. Run the following command to start Minikube with Docker as the driver:
   ```sh
   minikube start --driver=docker
   ```

## 3. Create a Docker Image for Flask

1. Create a `Dockerfile` for your Flask application. For example:
   ```Dockerfile
   # Use the official Python image from the Docker Hub
   FROM python:3.9-slim

   # Set the working directory in the container
   WORKDIR /app

   # Copy the requirements file and install dependencies
   COPY requirements.txt requirements.txt
   RUN pip install -r requirements.txt

   # Copy the rest of the application code
   COPY . .

   # Set the environment variable for Flask
   ENV FLASK_APP=app.py

   # Expose the port the app runs on
   EXPOSE 5000

   # Run the Flask application
   CMD ["flask", "run", "--host=0.0.0.0"]
   ```

2. Build the Docker image:
   ```sh
   docker build -t flask-app .
   ```

## 4. Deploy Flask Application to Minikube

1. Create a Kubernetes deployment YAML file, e.g., `flask-deployment.yaml`:
   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: flask-app
   spec:
     replicas: 1
     selector:
       matchLabels:
         app: flask-app
     template:
       metadata:
         labels:
           app: flask-app
       spec:
         containers:
         - name: flask-app
           image: flask-app:latest
           ports:
           - containerPort: 5000
   ```

2. Create a service YAML file, e.g., `flask-service.yaml`:
   ```yaml
   apiVersion: v1
   kind: Service
   metadata:
     name: flask-service
   spec:
     selector:
       app: flask-app
     ports:
       - protocol: TCP
         port: 80
         targetPort: 5000
     type: NodePort
   ```

3. Apply the deployment and service files to Minikube:
   ```sh
   kubectl apply -f flask-deployment.yaml
   kubectl apply -f flask-service.yaml
   ```

## 5. Access the Flask Application

1. Get the Minikube service URL:
   ```sh
   minikube service flask-service --url
   ```

2. Open the provided URL in your browser/Postman to access your Flask application.



