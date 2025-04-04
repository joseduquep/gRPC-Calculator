import grpc
from concurrent import futures
import time

import sum_pb2
import sum_pb2_grpc

class SumServiceServicer(sum_pb2_grpc.SumServiceServicer):
    def DoSum(self, request, context):
        print("[sum_service] Recibí petición de suma")
        a = request.a
        b = request.b
        result = a + b
        return sum_pb2.SumReply(result=result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sum_pb2_grpc.add_SumServiceServicer_to_server(
        SumServiceServicer(), server
    )
    server.add_insecure_port('[::]:50051')
    print("[sum_service] Iniciando servidor gRPC en puerto 50051...")
    server.start()
    try:
        while True:
            time.sleep(86400)  # Mantener el servidor corriendo
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
