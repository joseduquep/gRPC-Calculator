FROM python:3.9-slim

WORKDIR /app

# Copiar e instalar requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todos los archivos .proto antes de compilarlos
COPY sum.proto .
COPY sub.proto .
COPY mul.proto .
COPY div.proto .

# Compilar los .proto a archivos .py (pb2 y pb2_grpc)
RUN python -m grpc_tools.protoc \
    --proto_path=. \
    --python_out=. \
    --grpc_python_out=. \
    sum.proto sub.proto mul.proto div.proto

# Copiar el código del gateway (después de compilar los .proto)
COPY gateway.py .

EXPOSE 8000

CMD ["uvicorn", "gateway:app", "--host", "0.0.0.0", "--port", "8000"]
