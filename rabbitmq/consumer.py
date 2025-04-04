import os
import pika
import grpc
import time
import ast

import sum_pb2
import sum_pb2_grpc
import sub_pb2
import sub_pb2_grpc
import mul_pb2
import mul_pb2_grpc
import div_pb2
import div_pb2_grpc

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
    """
    body es un string que representa un diccionario con keys: { op, a, b }
    Ejemplo: "{'op': 'sum', 'a': 3.2, 'b': 4.5}"
    """
    message_str = body.decode('utf-8')
    data = ast.literal_eval(message_str)  # Convertir string -> dict
    op = data.get("op")
    a = float(data.get("a", 0))
    b = float(data.get("b", 0))

    print(f"[rabbitmq_consumer] Recibí mensaje en cola {method.routing_key}: {data}")

    try:
        if op == "sum":
            call_sum_service(a, b)
        elif op == "sub":
            call_sub_service(a, b)
        elif op == "mul":
            call_mul_service(a, b)
        elif op == "div":
            call_div_service(a, b)
    except Exception as e:
        print(f"[rabbitmq_consumer] Error procesando mensaje {data}: {e}")

    # Confirmar (ACK) que hemos procesado el mensaje
    ch.basic_ack(delivery_tag=method.delivery_tag)

def main():
    credentials = pika.PlainCredentials(RABBIT_USER, RABBIT_PASS)

    while True:
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=RABBIT_HOST, credentials=credentials)
            )
            channel = connection.channel()

            # Declarar las colas que escucharemos
            channel.queue_declare(queue="sum_queue", durable=True)
            channel.queue_declare(queue="sub_queue", durable=True)
            channel.queue_declare(queue="mul_queue", durable=True)
            channel.queue_declare(queue="div_queue", durable=True)

            # Consumir de cada cola
            channel.basic_consume(queue="sum_queue", on_message_callback=callback)
            channel.basic_consume(queue="sub_queue", on_message_callback=callback)
            channel.basic_consume(queue="mul_queue", on_message_callback=callback)
            channel.basic_consume(queue="div_queue", on_message_callback=callback)

            print("[rabbitmq_consumer] Esperando mensajes en sum_queue, sub_queue, mul_queue, div_queue")
            channel.start_consuming()
        except pika.exceptions.AMQPConnectionError as e:
            print("[rabbitmq_consumer] No se pudo conectar a RabbitMQ, reintentando en 5s...")
            time.sleep(5)
        except KeyboardInterrupt:
            print("[rabbitmq_consumer] Saliendo...")
            break

if __name__ == "__main__":
    main()
