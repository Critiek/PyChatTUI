import socket
from textual.app import App

def get_local_ipv4():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]

HOST = get_local_ipv4()

conn, addr = None, None

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def host_p2p(HOST, PORT):
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    return conn, addr


p2p_status = input("Connect or host? ['connect', 'host']\n> ").lower()

if p2p_status == "host":
    PORT = int(input("What port would you like to use?\n> "))
    conn, addr = host_p2p(HOST, PORT)

elif p2p_status == "connect":
    ipv4_port = input("Enter remote address and port formatted as [ipv4:port]\n> ")
    ipv4_port = ipv4_port.split(':')
    remote_addr = ipv4_port[0]
    remote_port = int(ipv4_port[1])
    s.connect((remote_addr, remote_port))


s.close()

# s.bind((HOST, PORT))
# s.listen()
# conn, addr = s.accept()
# with conn:
#     print(f"Connected by {}")
#     while True:
#         message = conn.recv(1024)
#         if not message:
#             break
#         print(message.decode('utf-8'))

'''
class MyApp(App):
    pass


if __name__ == "__main__":
    app = MyApp()
    app.run()
'''
