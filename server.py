import os
import time
import socket

localIP=input("local ip: ")
print(localIP)
localPORT=int(input("port: "))
messagesize=1024

ServerSock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
ServerSock.bind((localIP, localPORT))

print("listening")

while True:
    bap = ServerSock.recvfrom(messagesize)
    message=bap[0]
    addr=bap[1]
    print("message: ", message, " from: ", addr)
