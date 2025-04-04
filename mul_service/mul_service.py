import grpc
from concurrent import futures
import time

import mul_pb2
import mul_pb2_grpc

class MulServiceServicer(mul_pb2_grpc.MulServiceServicer):
    def DoMul(self, request, context):
        print("[mul_service] Recibí petición de multiplicación")
        a = request.a
        b = request.b
        result = a * b
        return mul_pb2.MulReply(result=result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mul_pb2_grpc.add_MulServiceServicer_to_server(
        MulServiceServicer(), server
    )
    server.add_insecure_port('[::]:50053')
    print("[mul_service] Iniciando servidor gRPC en puerto 50053...")
    server.start()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
