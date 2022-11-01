import os
import time
import socket
import json

datafile = open("data.json", "r+", encoding='utf-8')
data = json.load(datafile)

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

    y=data[addr]

    print("message: ", message, " from: ", addr)

datafile.seek(0)
datafile.truncate()
json.dump(data, datafile)
datafile.close()