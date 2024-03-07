import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def host(HOST, PORT):
    s.bind((HOST, PORT))
    s.listen(5)
    print(f"Listening on {(HOST, PORT)}")
    # s.setblocking(False)
    # sel.register(s, selectors.EVENT_READ, data=None)
    conn, addr = s.accept()
    return conn, addr
