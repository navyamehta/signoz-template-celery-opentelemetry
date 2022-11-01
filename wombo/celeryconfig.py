from kombu.utils.url import safequote
from wombo import config

aws_access_key = safequote(config.AWS_ACCESS_KEY_ID)
aws_secret_key = safequote(config.AWS_SECRET_ACCESS_KEY)

broker_url = "sqs://{aws_access_key}:{aws_secret_key}@sqs.us-east-1.amazonaws.com/426780362668/{sqsurl}".format(
    aws_access_key=aws_access_key, aws_secret_key=aws_secret_key, sqsurl=config.QUEUE_ENDPOINT,
)
task_acks_late = True
worker_prefetch_multiplier = 1
worker_concurrency = config.CELERY_WORKER_CONCURRENCY
