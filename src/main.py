import socket
from textual.app import App


s = socket.socket()
host = socket.gethostname()
port = 12345

print(host)


'''
class MyApp(App):
    pass


if __name__ == "__main__":
    app = MyApp()
    app.run()
'''
