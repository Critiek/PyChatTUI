import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def get_ip_port(input_text):
    ipv4_port = input_text.split(':')
    remote_addr = ipv4_port[0]
    remote_port = int(ipv4_port[1])
    return remote_addr, remote_port
