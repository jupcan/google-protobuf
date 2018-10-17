#!/usr/bin/python3
import socket
from student_pb2 import Student

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 2000))
student = Student()

while True:
    data, address = sock.recvfrom(1024)
    print("student address: {}, raw-data: {}".format(address, data))

    student.ParseFromString(data)
    print("Nombre: {0.firstname} \nApellidos: {0.lastname} \nDNI: {0.DNI} ({1})".format(
        student, Student.StudentType.Name(student.type)))
