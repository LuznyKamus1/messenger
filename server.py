import os
import time
import socket
import json

datafile = open("data.json", "r+", encoding='utf-8')
data = json.load(datafile)

localIP=input("local ip: ")
print(localIP)
localPORT=int(input("port: "))
messagesize=2048

ServerSock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
ServerSock.bind((localIP, localPORT))

print("listening")

while True:
    try:
        bap = ServerSock.recvfrom(messagesize)
        message=bap[0]
        addr=bap[1]

        try:
            y=data[str(addr)]
            y=str(message)
        except KeyError:
            data.update({str(addr):str(message)})

        ServerSock.sendto(str.encode("OK"), addr)
        print("message: ", str(message), " from: ", addr)
    except KeyboardInterrupt:
        datafile.seek(0)
        datafile.truncate()
        json.dump(data, datafile)
        datafile.close()
        exit()