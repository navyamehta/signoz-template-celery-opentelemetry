import os
import importlib
import logging
from typing import Dict, Any
from kombu import Queue
from celery import Celery
from celery.signals import setup_logging
from opentelemetry.sdk._logs import LoggingHandler
from wombo import config, metrics
from celery.signals import setup_logging
from opentelemetry.sdk._logs import LoggingHandler

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
logger.info(f"Initialized celerypaint for queue {config.QUEUE_ENDPOINT}")


@setup_logging.connect
def setup_loggers(*args, **kwargs):
    logger = logging.getLogger()
    logger.addHandler(LoggingHandler())
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stream = logging.StreamHandler()
    stream.setFormatter(formatter)
    logger.addHandler(stream)


@setup_logging.connect
def setup_loggers(*args, **kwargs):
    # OTEL Handler
    logger = logging.getLogger()
    logger.addHandler(LoggingHandler())

    # Stdout Handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    sh = logging.StreamHandler()
    sh.setFormatter(formatter)
    logger.addHandler(sh)


@celeryapp.task(name="WomboPaint")
def handle_paint_task(params_dict: Dict[str, Any]):
    metrics.requests_counter.add(1)
    logger.warning("SEE THIS WARNING BEING EMITTED")
    logger.info(f"{params_dict}")
