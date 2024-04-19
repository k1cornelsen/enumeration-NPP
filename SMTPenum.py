#!/usr/bin/python3
import socket 
import sys

if len(sys.argv) != 3:
    print("Modo de uso: python3 smtpenum.py IP usuario")
    sys.exit(1)

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((sys.argv[1], 25))
banner = tcp.recv(1024).decode('utf-8')
print(banner)

tcp.send(("VRFY " + sys.argv[2] + "\r\n").encode('utf-8'))
user = tcp.recv(1024).decode('utf-8')
print(user)

