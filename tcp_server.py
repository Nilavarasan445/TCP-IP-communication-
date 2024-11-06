import socket
import threading
from protocols import Protocol

class TCPServer:
    def __init__(self, host=socket.gethostname(), port=9999, protocol: Protocol = None):
        self.host = host
        self.port = port
        self.server_socket = None

    def protocol_handler(self, data, c_address):
        command = data.decode('utf-8').split(':')[0]
        if command == "READ":
            response = f"Reading data for {c_address}"
        elif command == "WRITE":
            response = f"Writing data for {c_address}"
        else:
            response = "Unknown command"
        return response

    def process_client(self, client_socket, c_address):
        try:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    print(f"No data received from {c_address}, closing connection.")
                    break

                print(f"Received data from {c_address}: {data.decode('utf-8')}")
                response = self.protocol_handler(data, c_address)
                client_socket.sendall(response.encode('utf-8'))

        except Exception as e:
            print(f"Error handling client {c_address}: {e}")
        finally:
            client_socket.close()

    def start_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(10)
        print(f"Server started at {self.host}:{self.port}.")

        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Connection from {client_address} established.")
            
            client_thread = threading.Thread(target=self.process_client, args=(client_socket, client_address))
            client_thread.start()

if __name__ == '__main__':
    server = TCPServer()
    server.start_server()
