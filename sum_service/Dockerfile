# sum_service/Dockerfile

FROM python:3.9-slim

WORKDIR /app

# Copiamos el requirements e instalamos
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el proto y el servicio
COPY sum.proto /app
COPY sum_service.py /app

# Generamos los archivos pb2
RUN python -m grpc_tools.protoc \
    --proto_path=/app \
    --python_out=/app \
    --grpc_python_out=/app \
    /app/sum.proto

EXPOSE 50051

CMD ["python", "sum_service.py"]
