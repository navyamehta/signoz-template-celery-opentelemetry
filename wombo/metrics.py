from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.resources import SERVICE_NAME, Resource

from wombo.config import OTEL_SERVICE_NAME

# opentelemetry-instrument already does this for us

# resource = Resource(attributes={
#     SERVICE_NAME: OTEL_SERVICE_NAME
# })
# provider = MeterProvider(resource=resource)
# metrics.set_meter_provider(provider)
meter = metrics.get_meter("worker_vqgan")

requests_counter = meter.create_counter(
    name="requests",
    description="number of requests"
)

