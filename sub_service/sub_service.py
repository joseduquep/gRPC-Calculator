import grpc
from concurrent import futures
import time

import sub_pb2
import sub_pb2_grpc

class SubServiceServicer(sub_pb2_grpc.SubServiceServicer):
    def DoSub(self, request, context):
        print("[sub_service] Recibí petición de resta")
        a = request.a
        b = request.b
        result = a - b
        return sub_pb2.SubReply(result=result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sub_pb2_grpc.add_SubServiceServicer_to_server(
        SubServiceServicer(), server
    )
    server.add_insecure_port('[::]:50052')
    print("[sub_service] Iniciando servidor gRPC en puerto 50052...")
    server.start()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
