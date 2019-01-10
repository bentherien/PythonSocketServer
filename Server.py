'''
Created on Mar 12, 2018

@author: BenjaminTherien
'''
import socketserver
from BaseFunctions import *
from ServerFunctions import *
import json

#this puts the information from the database into a deque
dq= getData("data.txt")    

class MyUDPHandler(socketserver.BaseRequestHandler):
#the following method is used to handle any requests a client can make to the server  
    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        info= tuple(json.loads(data.decode("utf-8")))
#the following if-else statements are used to send the correct information to the client 
#based on the input the initially sent the server
        if info[0] == "1":
            socket.sendto(findC(info[1],dq).encode("utf-8"), self.client_address)
        elif info[0] == "2" :
            socket.sendto(addC((info[1],info[2],info[3],info[4]),dq).encode("utf-8"), self.client_address)
        elif info[0] == "3" :
            socket.sendto(delC(info[1],dq).encode("utf-8"), self.client_address)
        elif info[0] == "4" :
            socket.sendto(updAge(info[1],info[2],dq).encode("utf-8"), self.client_address)
        elif info[0] == "5" :
            socket.sendto(updA(info[1],info[2],dq).encode("utf-8"), self.client_address)
        elif info[0] == "6" :
            socket.sendto(updN(info[1],info[2],dq).encode("utf-8"), self.client_address)
        elif info[0] == "7" :
            socket.sendto(printReport(dq).encode("utf-8"), self.client_address)
        else:
            socket.sendto("please enter a valid number".encode("utf-8"), self.client_address)


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    server = socketserver.UDPServer((HOST, PORT), MyUDPHandler)    
    server.serve_forever()