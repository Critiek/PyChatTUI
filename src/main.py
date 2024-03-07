import socket

client_type = input("Host or connect? ['host', 'connect']\n> ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
