"""
This simulates a SNMP device which sends information through UDP port 162
"""
import sys
import socket
from time import sleep

UDP_IP = "localhost"
UDP_PORT = 162
MESSAGE = "SNMP SNMP SNMP"

clt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    try:
        clt.sendto(bytes(MESSAGE,"utf-8"),(UDP_IP,UDP_PORT))
        print("message sent is:  ",MESSAGE)
        sleep(10)
    except KeyboardInterrupt:
        clt.sendto(bytes("quit","utf-8"),(UDP_IP,UDP_PORT))
        clt.close()
        exit()
