import grpc
from concurrent import futures
import time

import div_pb2
import div_pb2_grpc

class DivServiceServicer(div_pb2_grpc.DivServiceServicer):
    def DoDiv(self, request, context):
        print("[div_service] Recibí petición de división")
        a = request.a
        b = request.b
        # Manejar caso b=0 de modo simple
        if b == 0:
            return div_pb2.DivReply(result=0.0)
        result = a / b
        return div_pb2.DivReply(result=result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    div_pb2_grpc.add_DivServiceServicer_to_server(
        DivServiceServicer(), server
    )
    server.add_insecure_port('[::]:50054')
    print("[div_service] Iniciando servidor gRPC en puerto 50054...")
    server.start()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
