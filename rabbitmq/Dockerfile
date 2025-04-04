FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY consumer.py /app
COPY producer.py /app  # (Opcional, si quieres mantener la lógica de producer)

CMD ["python", "consumer.py"]
