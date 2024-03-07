import socket

client_type = input("Host or connect? ['host', 'connect']\n> ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if client_type == 'host':
    s.bind(('127.0.0.1', 12345))    
    s.listen(5)  # Listen for incoming connections
    conn, addr = s.accept()
    print(f"Connected by {addr}")
    while True:
        msg = ''
        msg = conn.recv(1024)
        msg = msg.decode('utf-8')
        print(msg)
        
elif client_type == 'connect':
    s.connect(('127.0.0.1', 12345))
    while True:
        msg = input("Enter message: ")
        s.sendall(msg.encode('utf-8'))