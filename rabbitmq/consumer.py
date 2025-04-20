import os
import pika
import grpc
import time
import ast
import os
os.environ["PYTHONUNBUFFERED"] = "1"

import sum_pb2
import sum_pb2_grpc
import sub_pb2
import sub_pb2_grpc
import mul_pb2
import mul_pb2_grpc
import div_pb2
import div_pb2_grpc

print("🟢 [INICIO] El archivo consumer.py se está ejecutando.")
RABBIT_HOST = os.getenv("RABBIT_HOST", "rabbitmq-broker")
RABBIT_USER = os.getenv("RABBIT_USER", "admin")
RABBIT_PASS = os.getenv("RABBIT_PASS", "admin")

def call_sum_service(a, b):
    with grpc.insecure_channel("sum_service:50051") as channel:
        stub = sum_pb2_grpc.SumServiceStub(channel)
        request = sum_pb2.SumRequest(a=a, b=b)
        response = stub.DoSum(request)
    print(f"[rabbitmq_consumer] Suma procesada: {a} + {b} = {response.result}")

def call_sub_service(a, b):
    with grpc.insecure_channel("sub_service:50052") as channel:
        stub = sub_pb2_grpc.SubServiceStub(channel)
        request = sub_pb2.SubRequest(a=a, b=b)
        response = stub.DoSub(request)
    print(f"[rabbitmq_consumer] Resta procesada: {a} - {b} = {response.result}")

def call_mul_service(a, b):
    with grpc.insecure_channel("mul_service:50053") as channel:
        stub = mul_pb2_grpc.MulServiceStub(channel)
        request = mul_pb2.MulRequest(a=a, b=b)
        response = stub.DoMul(request)
    print(f"[rabbitmq_consumer] Multiplicación procesada: {a} * {b} = {response.result}")

def call_div_service(a, b):
    with grpc.insecure_channel("div_service:50054") as channel:
        stub = div_pb2_grpc.DivServiceStub(channel)
        request = div_pb2.DivRequest(a=a, b=b)
        response = stub.DoDiv(request)
    print(f"[rabbitmq_consumer] División procesada: {a} / {b} = {response.result}")

def callback(ch, method, properties, body):
    data = ast.literal_eval(body.decode())
    op = data["op"]
    a = data["a"]
    b = data["b"]

    print(f"[{time.strftime('%H:%M:%S')}] 📥 Mensaje recibido en {method.routing_key}: {data}")

    try:
        if op == "sum":
            with grpc.insecure_channel("sum_service:50051") as channel:
                stub = sum_pb2_grpc.SumServiceStub(channel)
                request = sum_pb2.SumRequest(a=a, b=b)
                response = stub.DoSum(request, timeout=3)  # 🔥 Agregado timeout
                print(f"[{time.strftime('%H:%M:%S')}] ✅ Resultado suma: {a} + {b} = {response.result}")

        elif op == "sub":
            with grpc.insecure_channel("sub_service:50052") as channel:
                stub = sub_pb2_grpc.SubServiceStub(channel)
                request = sub_pb2.SubRequest(a=a, b=b)
                response = stub.DoSub(request, timeout=3)
                print(f"[{time.strftime('%H:%M:%S')}] ✅ Resultado resta: {a} - {b} = {response.result}")

        elif op == "mul":
            with grpc.insecure_channel("mul_service:50053") as channel:
                stub = mul_pb2_grpc.MulServiceStub(channel)
                request = mul_pb2.MulRequest(a=a, b=b)
                response = stub.DoMul(request, timeout=3)
                print(f"[{time.strftime('%H:%M:%S')}] ✅ Resultado multiplicación: {a} * {b} = {response.result}")

        elif op == "div":
            with grpc.insecure_channel("div_service:50054") as channel:
                stub = div_pb2_grpc.DivServiceStub(channel)
                request = div_pb2.DivRequest(a=a, b=b)
                response = stub.DoDiv(request, timeout=3)
                print(f"[{time.strftime('%H:%M:%S')}] ✅ Resultado división: {a} / {b} = {response.result}")

        # Si todo funcionó → acknowledge (confirmar)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    except grpc.RpcError as e:
        print(f"[{time.strftime('%H:%M:%S')}] ❌ Error gRPC procesando {data}: {e.details()}")
        time.sleep(5)
        raise

    except Exception as e:
        print(f"[{time.strftime('%H:%M:%S')}] ❌ Error general procesando {data}: {e}")
        time.sleep(5)
        raise

def main():
    print(f"[{time.strftime('%H:%M:%S')}] 🔁 Entrando a bucle principal...")
    credentials = pika.PlainCredentials(RABBIT_USER, RABBIT_PASS)

    while True:
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=RABBIT_HOST, credentials=credentials)
            )
            channel = connection.channel()

            # Declarar las colas que escucha
            channel.queue_declare(queue="sum_queue", durable=True)
            channel.queue_declare(queue="sub_queue", durable=True)
            channel.queue_declare(queue="mul_queue", durable=True)
            channel.queue_declare(queue="div_queue", durable=True)

            # Consumir cada cola
            channel.basic_consume(queue="sum_queue", on_message_callback=callback, auto_ack=False)
            channel.basic_consume(queue="sub_queue", on_message_callback=callback, auto_ack=False)
            channel.basic_consume(queue="mul_queue", on_message_callback=callback, auto_ack=False)
            channel.basic_consume(queue="div_queue", on_message_callback=callback, auto_ack=False)

            print(f"[{time.strftime('%H:%M:%S')}] ✅ Escuchando sum_queue, sub_queue, mul_queue, div_queue...")

            try:
                channel.start_consuming()
            except Exception as e:
                print(f"[{time.strftime('%H:%M:%S')}] ⚠️ Error interno en start_consuming: {e}")
                channel.stop_consuming()
                time.sleep(5)

        except pika.exceptions.AMQPConnectionError as e:
            print(f"[{time.strftime('%H:%M:%S')}] ❌ Error de conexión con RabbitMQ: {e}")
            time.sleep(5)

if __name__ == "__main__":
    main()
