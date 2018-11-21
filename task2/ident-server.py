#!/usr/bin/python3
# -*- coding:utf-8; mode:python -*-
import time
import grpc
import exercise_pb2
import exercise_pb2_grpc
from concurrent import futures

DAY_SECONDS = 24*60*60

class Ident(exercise_pb2_grpc.IdentServicer):
    def getID (self, request, context):
        DNI="00000000A-Z"
        fname="Juan Perea"
        return exercise_pb2.GetIdReply(dni=DNI, fullname=fname)

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
exercise_pb2_grpc.add_IdentServicer_to_server(Ident(), server)
server.add_insecure_port('0.0.0.0:2000')
server.start()

try:
    while True:
        time.sleep(DAY_SECONDS)

except KeyboardInterrupt:
    server.stop(0)
