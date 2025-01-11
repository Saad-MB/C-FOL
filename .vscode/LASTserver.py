#!/usr/bin/env python

from __future__ import print_function
from socket import *
import random

bind = '' #listen on any
port = 25050
LOSS_RATE = 0.3
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((bind, port))
print(port)
while True:
    message, address = serverSocket.recvfrom(2048)
    print("Received from:", address, end='\n', flush=True)
    RandNum = random.random()
    if RandNum < LOSS_RATE:
     print ("Reply not sent. ")
    else: 
     serverSocket.sendto(message, address)
     print("Reply sent.", end='\n', flush=True)   
    
