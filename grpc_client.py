import grpc

import user_service_pb2_grpc
import user_service_pb2

channel = grpc.insecure_channel('localhost:50051')
stub = user_service_pb2_grpc.UserServiceStub(channel)

resource = stub.GetUser(user_service_pb2.GetUserRequest(username="Alice"))
print(resource)