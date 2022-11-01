import os

def get_boolean_from_os(field, default):
    return str(os.getenv(field, default)).lower() == "true"

# Infrastructure settings
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
PAINTS_BUCKET = os.getenv("PAINTS_BUCKET")
MEDIASTORE_BUCKET = os.getenv("MEDIASTORE_BUCKET")

# OpenTelemetry
OTEL_EXPORTER_OTLP_INSECURE = get_boolean_from_os("OTEL_EXPORTER_OTLP_INSECURE", True)
# Should be ideally APP_NAME_dev, APP_NAME_staging, APP_NAME_abhinav etc.
OTEL_SERVICE_NAME = os.getenv("OTEL_SERVICE_NAME", "VQGAN-celery")
# GRPC port because HTTP doesn't support both metrics and traces
OTEL_EXPORTER_OTLP_ENDPOINT = os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT", "http://44.193.198.87:4317")

GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
PRODUCTION = get_boolean_from_os("PRODUCTION", False)

# Run-time settings
STATUS_CALLBACK_ENDPOINT = os.getenv("STATUS_CALLBACK_ENDPOINT")
USE_WEBSOCKET_INFRA = get_boolean_from_os("USE_WEBSOCKET_INFRA", False)

# Database settings
MEDIASTORE_DATABASE_URL = os.getenv("MEDIASTORE_DATABASE_URL")
CONCURRENCY = int(os.getenv("CONCURRENCY", 1))
MAXOVERFLOW = int(os.getenv("MAXOVERFLOW", 1))
ENABLE_FIRST_LOCK = get_boolean_from_os("ENABLE_FIRST_LOCK", True)
ENABLE_SUBSEQUENT_LOCKS = get_boolean_from_os("ENABLE_SUBSEQUENT_LOCKS", False)

# Generation settings
FAST_TEXT_MODEL = os.getenv("FAST_TEXT_MODEL")
QUEUE_ENDPOINT = os.getenv("QUEUE_ENDPOINT")
# Counter to see how many tasks have been completed
MAX_CREATIONS = int(os.getenv("MAX_CREATIONS_PER_WORKER", 50))
CELERY_WORKER_CONCURRENCY = int(os.getenv("CELERY_WORKER_CONCURRENCY", 2))
