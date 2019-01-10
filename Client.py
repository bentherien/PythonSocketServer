'''
Created on Mar 12, 2018

@author: BenjaminTherien
'''
import socket
import sys
from BaseFunctions import *
from ServerFunctions import *
import json

HOST, PORT = "localhost", 9999

while True:
    number = input("""Python DB Menu:
1. Find customer
2. Add customer
3. Delete customer
4. Update customer age
5. Update customer address
6. Update customer phone 
7. Print report
8. Exit 
Select:""")
#the following series of if-else statements are used to send the correct information to the server base
# on the option selected by the user
    if number == "8" :
        print("Quitting client, 'sayonara, sweet-heart' \n")
        sys.exit(0)
    elif number == "1":
        name = input("Enter the name of the customer to find: ")
        data = json.dumps((" ".join(str(number)),name))
    elif number == "2":
        name= input("Enter customer name:")
        age= input("Enter customer age:")
        address= input("Enter customer address:")
        pnum= input("Enter customer phone number:")
        data = json.dumps((" ".join(str(number)),name,age,address,pnum))
    elif number == "3":
        name = input("Enter the name of the customer to delete: ")
        data = json.dumps((" ".join(str(number)),name))
    elif number == "4":
        name = input("Enter the name of the customer to modify:")
        age=input("Enter the new age: ")
        data = json.dumps((" ".join(str(number)),name,age))
    elif number == "5":
        name = input("Enter the name of the customer to modify: ")
        add=input("Enter the new address: ")
        data = json.dumps((" ".join(str(number)),name,add))
    elif number == "6":
        name = input("Enter the name of the customer to modify: ")
        num=input("Enter the new phone number: ")
        data = json.dumps((" ".join(str(number)),name,num))
    elif number == "7":
        data = json.dumps(" ".join(str(number)),)
        
    else:
        data = json.dumps(" ".join(str(number)),)

    # SOCK_DGRAM is the socket type to use for UDP sockets
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    #sending "data" to the server
    sock.sendto(bytes(data, "utf-8"), (HOST, PORT))
    #getting info received from server
    received = str(sock.recv(1024), "utf-8")
    print("\n{} \n".format(received))