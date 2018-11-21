#!/usr/bin/python3
# -*- coding:utf-8; mode:python -*-
from concurrent import futures
import time
import grpc
import exercise_pb2
import exercise_pb2_grpc

DAY_SECONDS = 24*60*60

class Check(exercise_pb2_grpc.CheckServicer):
    def checkme (self, request, context):
        return exercise_pb2.CheckmeReply()

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
exercise_pb2_grpc.add_CheckServicer_to_server(Check(), server)
server.add_insecure_port('0.0.0.0:2000')
server.start()

try:
    while True:
        time.sleep(DAY_SECONDS)

except KeyboardInterrupt:
    server.stop(0)
