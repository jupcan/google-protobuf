#!/usr/bin/python3
# -*- coding:utf-8; mode:python -*-
import sys
import grpc
import exercise_pb2
import exercise_pb2_grpc

if len(sys.argv) != 4:
    print("usage: ./client <check-server-host> <ident-server-host> <ident-server-port>")
    sys.exit(1)

server = sys.argv[1]
ident_host = sys.argv[2]
ident_port = int(sys.argv[3])

channel = grpc.insecure_channel('{}:2000'.format(server))
stub = exercise_pb2_grpc.CheckStub(channel)
response = stub.checkme(exercise_pb2.CheckmeRequest(host=ident_host, port=ident_port))
print("result = '{}'".format(response.result))
