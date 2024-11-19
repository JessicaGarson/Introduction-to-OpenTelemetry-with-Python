# Running the Flask examples

## Step 1: Install the required packages

```
pip install elastic-opentelemetry opentelemetry-api opentelemetry-sdk opentelemetry-exporter-otlp opentelemetry-instrumentation-flask
opentelemetry-bootstrap --action=install
```

## Step 2: Setting local environment variables 

```
export OTEL_RESOURCE_ATTRIBUTES=service.name=todo-list-app
export OTEL_EXPORTER_OTLP_HEADERS="Authorization=Bearer <your-auth-token>"
export OTEL_EXPORTER_OTLP_ENDPOINT=https://<your-elastic-cloud-url>
export ELASTIC_OTEL_SYSTEM_METRICS_ENABLED=true
```

## Step 3: Running the app

### Automatic instrumentation

```
opentelemetry-instrument python app.py
```

### Manual instrumentation

```
flask run -p 5000
```
