FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY sub.proto /app
COPY sub_service.py /app

RUN python -m grpc_tools.protoc \
    --proto_path=/app \
    --python_out=/app \
    --grpc_python_out=/app \
    /app/sub.proto

EXPOSE 50052

CMD ["python", "sub_service.py"]
