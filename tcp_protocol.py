import socket
from protocols import Protocol

class TCPProtocol(Protocol):
    def __init__(self):
        self.client_socket = None

    def connect(self, host, port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))
        print(f"Connected to server at {host}:{port}")

    def send_data(self, data):
        self.client_socket.sendall(data.encode('utf-8'))

    def receive_data(self):
        return self.client_socket.recv(1024).decode('utf-8')

    def close_connection(self):
        if self.client_socket:
            self.client_socket.close()
            print("Connection closed.")
