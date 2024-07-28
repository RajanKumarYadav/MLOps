
```markdown
# Setting Up Minikube on Windows and Running a Flask Docker Application

This guide provides step-by-step instructions to install Minikube on a local Windows machine and deploy a Flask Docker application.

## Prerequisites

- **Windows 10/11**
- **Docker Desktop** installed and running
- **Kubernetes** enabled in Docker Desktop
- **PowerShell** or **Command Prompt**

## Steps

### 1. Install Minikube

1. Download and install Minikube using the installer:
   - Download the latest Minikube installer from the [Minikube Releases page](https://github.com/kubernetes/minikube/releases).
   - Run the installer and follow the installation steps.

2. Verify the installation by opening a new terminal and running:
   ```sh
   minikube version
   ```

### 2. Start Minikube

Start Minikube with the Docker driver:
```sh
minikube start --driver=docker
```

### 3. Configure Docker to Use Minikube’s Docker Daemon

#### Using PowerShell

1. Open PowerShell as Administrator.
2. Run the following command to configure Docker to use Minikube's Docker daemon:
   ```powershell
   & minikube -p minikube docker-env | Invoke-Expression
   ```

#### Using Command Prompt

1. Open Command Prompt.
2. Run the following command and follow the output instructions:
   ```cmd
   minikube -p minikube docker-env --shell cmd
   ```

### 4. Build the Docker Image

1. Navigate to the directory containing your `Dockerfile`.
2. Build the Docker image:
   ```sh
   docker build -t diabetes_prediction_app:0.0.11 .
   ```

### 5. Create Kubernetes Deployment and Service YAML Files

Create `deployment.yaml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: diabetes-prediction-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: diabetes-prediction-app
  template:
    metadata:
      labels:
        app: diabetes-prediction-app
    spec:
      containers:
      - name: diabetes-prediction-app
        image: diabetes_prediction_app:0.0.11
        ports:
        - containerPort: 5000
```

Create `service.yaml`:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: diabetes-prediction-app-service
spec:
  selector:
    app: diabetes-prediction-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 5000
  type: LoadBalancer
```

### 6. Apply the Kubernetes Deployment and Service

1. Apply the deployment:
   ```sh
   kubectl apply -f deployment.yaml
   ```

2. Apply the service:
   ```sh
   kubectl apply -f service.yaml
   ```

### 7. Verify the Deployment

1. Check the status of the pods:
   ```sh
   kubectl get pods
   ```

2. If the pod is not running, describe it for more details:
   ```sh
   kubectl describe pod <pod-name>
   ```

### 8. Access Your Flask Application

Get the URL to access your Flask application:
```sh
minikube service diabetes-prediction-app-service --url
```

Open the provided URL in your browser to see your Flask application.

## Troubleshooting

- If you encounter an `ImagePullBackOff` error, ensure the image is built within Minikube’s Docker environment.
- Ensure Minikube has internet access:
  ```sh
  minikube ssh -- curl -I https://registry.hub.docker.com
  ```

```

