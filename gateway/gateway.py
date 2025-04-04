from fastapi import FastAPI
import uvicorn
import grpc
import os
import pika

# Importamos los stubs de gRPC ya compilados
import sum_pb2
import sum_pb2_grpc
import sub_pb2
import sub_pb2_grpc
import mul_pb2
import mul_pb2_grpc
import div_pb2
import div_pb2_grpc

app = FastAPI(title="API Gateway")

RABBIT_HOST = os.getenv("RABBIT_HOST", "rabbitmq-broker")
RABBIT_USER = os.getenv("RABBIT_USER", "admin")
RABBIT_PASS = os.getenv("RABBIT_PASS", "admin")

def publish_to_rabbitmq(queue_name, payload):
    """Publica el payload (diccionario) en la cola indicada."""
    credentials = pika.PlainCredentials(RABBIT_USER, RABBIT_PASS)
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=RABBIT_HOST, credentials=credentials)
    )
    channel = connection.channel()
    channel.queue_declare(queue=queue_name, durable=True)
    channel.basic_publish(
        exchange='',
        routing_key=queue_name,
        body=str(payload).encode('utf-8')
    )
    connection.close()

@app.get("/")
def root():
    return {"message": "Gateway funcionando. Endpoints: /sum, /sub, /mul, /div"}

@app.get("/sum")
def do_sum(a: float, b: float):
    # Llamada gRPC a sum_service
    try:
        with grpc.insecure_channel("sum_service:50051") as channel:
            stub = sum_pb2_grpc.SumServiceStub(channel)
            request = sum_pb2.SumRequest(a=a, b=b)
            response = stub.DoSum(request)
            return {"operation": "sum", "a": a, "b": b, "result": response.result}
    except Exception as e:
        # Microservicio no disponible -> Enviar a cola
        payload = {"op": "sum", "a": a, "b": b}
        publish_to_rabbitmq("sum_queue", payload)
        return {"status": "queued", "details": str(e)}

@app.get("/sub")
def do_sub(a: float, b: float):
    try:
        with grpc.insecure_channel("sub_service:50052") as channel:
            stub = sub_pb2_grpc.SubServiceStub(channel)
            request = sub_pb2.SubRequest(a=a, b=b)
            response = stub.DoSub(request)
            return {"operation": "sub", "a": a, "b": b, "result": response.result}
    except Exception as e:
        payload = {"op": "sub", "a": a, "b": b}
        publish_to_rabbitmq("sub_queue", payload)
        return {"status": "queued", "details": str(e)}

@app.get("/mul")
def do_mul(a: float, b: float):
    try:
        with grpc.insecure_channel("mul_service:50053") as channel:
            stub = mul_pb2_grpc.MulServiceStub(channel)
            request = mul_pb2.MulRequest(a=a, b=b)
            response = stub.DoMul(request)
            return {"operation": "mul", "a": a, "b": b, "result": response.result}
    except Exception as e:
        payload = {"op": "mul", "a": a, "b": b}
        publish_to_rabbitmq("mul_queue", payload)
        return {"status": "queued", "details": str(e)}

@app.get("/div")
def do_div(a: float, b: float):
    try:
        with grpc.insecure_channel("div_service:50054") as channel:
            stub = div_pb2_grpc.DivServiceStub(channel)
            request = div_pb2.DivRequest(a=a, b=b)
            response = stub.DoDiv(request)
            return {"operation": "div", "a": a, "b": b, "result": response.result}
    except Exception as e:
        payload = {"op": "div", "a": a, "b": b}
        publish_to_rabbitmq("div_queue", payload)
        return {"status": "queued", "details": str(e)}

if __name__ == "__main__":
    uvicorn.run("gateway:app", host="0.0.0.0", port=8000, reload=False)
