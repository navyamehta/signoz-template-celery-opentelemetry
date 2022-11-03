import os
import importlib
import logging
from celery.signals import worker_process_init
from opentelemetry.instrumentation.celery import CeleryInstrumentor
from opentelemetry.instrumentation.logging import LoggingInstrumentor
from typing import Dict, Any
from kombu import Queue
from celery import Celery
from wombo import config, metrics

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Celery Initialization
celery_config_module = os.getenv('CELERY_CONFIG_MODULE', 'celeryconfig')
celeryconfig = importlib.import_module(f'.{celery_config_module}', package='wombo')
celeryapp = Celery('celerypaint')
celeryapp.config_from_object(celeryconfig)
celeryapp.conf.task_queues = (Queue(config.QUEUE_ENDPOINT),)
celeryapp.conf.task_default_queue = config.QUEUE_ENDPOINT
# logger.info(f"Initialized celerypaint for queue {config.QUEUE_ENDPOINT}")


# @worker_process_init.connect(weak=False)
# def init_celery_tracing(*args, **kwargs):
#     """
#     When tracing a celery worker process, tracing and instrumention both must be initialized after the celery worker
#     process is initialized. This is required for any tracing components that might use threading to work correctly
#     such as the BatchSpanProcessor. Celery provides a signal called worker_process_init that can be used to
#     accomplish this
#     """
#     #LoggingInstrumentor().instrument(set_logging_format=True)
#     #CeleryInstrumentor().instrument()
#     #logger.warning("Instrumentation of Celery initiated...")


@celeryapp.task(name="WomboPaint")
def handle_paint_task(params_dict: Dict[str, Any]):
    metrics.requests_counter.add(1)
    logger.warning("SEE THIS WARNING BEING EMITTED")
    logger.info(f"{params_dict}")
