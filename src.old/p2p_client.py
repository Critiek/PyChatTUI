import socket
import selectors
from textual.app import App
import host
import connect

sel = selectors.DefaultSelector()

def get_local_ipv4():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]


HOST = get_local_ipv4()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

conn, addr = None, None


p2p_status = input("Connect or host? ['connect', 'host']\n> ").lower()

if p2p_status == "host":
    PORT = int(input("What port would you like to use?\n> "))
    conn, addr = host.host(HOST, PORT)
    print(f"{addr} has connected")
    while True:
        s.sendall(bytes(input("> "), "utf-8"))

elif p2p_status == "connect":
    ipv4_port = input("Enter remote address and port formatted as [ipv4:port]\n> ")
    remote_addr, remote_port = connect.get_ip_port(ipv4_port)
    s.connect((remote_addr, remote_port))
    while True:
        msg = ''
        msg = s.recv(128)
        msg = msg.decode("utf-8")
        print(msg)




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
