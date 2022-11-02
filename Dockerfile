FROM python:3.9.5-slim

RUN DEBIAN_FRONTEND=noninteractive apt-get -qq update && \
    DEBIAN_FRONTEND=noninteractive apt-get -qqy --no-install-recommends install \
    ffmpeg git libxext6 libsm6 libcurl4-openssl-dev libssl-dev gcc musl-dev libc6-dev linux-libc-dev && \
    rm -rf /var/lib/apt/lists/*

RUN python -m pip install torch==1.13.0 numpy==1.23.4
COPY ./requirements.txt ./
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN opentelemetry-bootstrap --action=install

# restricts memory for strategies evaluated in cudnn benchmarking, needed to avoid OOM
ENV CUDNN_CONV_WSCAP_DBG=4096

COPY . /app/
WORKDIR /app
CMD opentelemetry-instrument --logs_exporter otlp_proto_grpc,console --traces_exporter otlp_proto_grpc,console celery -A wombo.celery_paint.celeryapp worker --loglevel=info