FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el .proto directamente desde la carpeta actual
COPY sum.proto /app
COPY sub.proto /app
COPY mul.proto /app
COPY div.proto /app

# Compilar el .proto dentro del contenedor
RUN python -m grpc_tools.protoc \
    --proto_path=/app \
    --python_out=/app \
    --grpc_python_out=/app \
    sum.proto sub.proto mul.proto div.proto

COPY consumer.py /app

CMD ["python", "consumer.py"]

