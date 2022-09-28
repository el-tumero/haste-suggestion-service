from concurrent import futures
import grpc
import suggestion_pb2
import suggestion_pb2_grpc
import numpy as np
from make_prediction import make_prediction

class SuggestionServicer(suggestion_pb2_grpc.SuggestionServicer):
    def getChance(self, request, context):
        chance = make_prediction(np.array(request.first), np.array(request.second))
        reply = suggestion_pb2.Reply()
        reply.chance = chance
        return reply

def serve():
    print("Server runs...")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    suggestion_pb2_grpc.add_SuggestionServicer_to_server(SuggestionServicer(), server)
    server.add_insecure_port("localhost:4000")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()