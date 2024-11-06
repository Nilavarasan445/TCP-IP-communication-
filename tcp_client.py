import socket
from protocols import Protocol

class TCPClient:
    def __init__(self, host=socket.gethostname(), port=9999, protocol: Protocol = None, use_stub=False):
        self.host = host
        self.port = port
        self.use_stub = use_stub

    def connect(self):
        if not self.use_stub:
            self.protocol.connect(self.host, self.port)
        else:
            print("Using stub for TCP connection.")

    def send_data(self, data):
        if self.use_stub:
            print(f"Stub: sending data '{data}'")
            return "Stub response"
        else:
            self.protocol.send_data(data)
            response = self.protocol.receive_data()
            print(f"Server response: {response}")
            return response

    def close_connection(self):
        if not self.use_stub:
            self.protocol.close_connection()
        else:
            print("Stub: closing connection.")

def connect_multiple_clients(use_stub=False):
    for i in range(5):
        client = TCPClient(use_stub=use_stub)
        client.connect()
        client.send_data(f"READ: Connection Request from client {i + 1}")
        client.send_data(f"WRITE: Connection Request from client {i + 1}")
        client.close_connection()

if __name__ == "__main__":
    connect_multiple_clients(use_stub=False)
