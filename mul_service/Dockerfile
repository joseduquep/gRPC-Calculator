FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY mul.proto /app
COPY mul_service.py /app

RUN python -m grpc_tools.protoc \
    --proto_path=/app \
    --python_out=/app \
    --grpc_python_out=/app \
    /app/mul.proto

EXPOSE 50053

CMD ["python", "mul_service.py"]
