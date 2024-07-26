# MLflow command to Run experiments

```bash
mlflow run . -P random_state=42 -P max_iter=100
```

```bash
mlflow run . -P random_state=42 -P max_iter=100 --experiment-name "MLflow-Project-1.0"
```


# MLflow commands 

### Start MLFlow UI
```bash
mlflow ui 
```

### Start the MLFlow Server
```bash
mlflow server --host 0.0.0.0 --port 5000
```

### Host and load the model to MLFlow Server 
```bash
mlflow models serve --model-uri runs:/<Run ID>/model --port 5021 --no-conda
```

```bash
mlflow models serve --model-uri runs:/203ab8be70d24f8486d67c0ae042cfae/model --port 5021 --no-conda
```

