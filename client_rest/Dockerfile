FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY client.py /app

EXPOSE 9000

CMD ["uvicorn", "client:app", "--host", "0.0.0.0", "--port", "9000"]
