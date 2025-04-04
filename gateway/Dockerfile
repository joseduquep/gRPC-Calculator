FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todos los .proto compilados (generados) si fuera necesario,
# pero aquí asumimos que los microservicios ya los exponen. 
# Para este Gateway, con las definiciones de proto basta con compilar localmente 
# o bien se pueden copiar. Dependiendo de cómo prefieras.



COPY gateway.py /app

EXPOSE 8000

CMD ["uvicorn", "gateway:app", "--host", "0.0.0.0", "--port", "8000"]
