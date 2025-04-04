FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY div.proto /app
COPY div_service.py /app

RUN python -m grpc_tools.protoc \
    --proto_path=/app \
    --python_out=/app \
    --grpc_python_out=/app \
    /app/div.proto

EXPOSE 50054

CMD ["python", "div_service.py"]
