# signoz-template-celery-opentelemetry
Debugging template for Signoz (Opentelemetry) with Celery. You can directly run 
```
./run_locally.sh
```
Otherwise, you can first install dependencies with
```
python -m pip install torch==1.13.0 numpy==1.23.4
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
opentelemetry-bootstrap --action=install
```
and then run
```
opentelemetry-instrument --logs_exporter otlp_proto_grpc,console --traces_exporter otlp_proto_grpc,console celery -A wombo.celery_paint.celeryapp worker --loglevel=info (maybe also add --pool=threads)
```