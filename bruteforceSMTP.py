#!/usr/bin/python3
import socket
import sys
import re

if len(sys.argv) != 2:
    print("Modo de uso: python smtpenum.py IP")
    sys.exit(1)

file = open("lista.txt")
for line in file:
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.connect((sys.argv[1], 25))
    banner = tcp.recv(1024)
    tcp.send(("VRFY " + line).encode('utf-8'))
    user = tcp.recv(1024).decode('utf-8')
    if re.search("252", user):
        print("Usuario encontrado: " + user.strip("252 2.0.0"))

file.close()

