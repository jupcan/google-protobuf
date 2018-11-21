#!/usr/bin/python3
import sys
import socket
import student_pb2

if len(sys.argv) < 2:
    print('usage: ./udp-client.py <host>')
    exit()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
destination = (sys.argv[1], 2000)

student = student_pb2.Student()
student.DNI = "00000000A-Z"
student.type = student_pb2.Student.PASS
student.firstname = "Juan"
student.lastname = "Perea"

data = student.SerializeToString()
sock.sendto(data, destination)
sock.close()
