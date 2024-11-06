# Protocol Communication System

This project demonstrates a client-server communication system that supports multiple protocols. It currently supports TCP/IP communication, but the design is flexible enough to add more protocols in the future.

## Features

- **TCP/IP Communication**: A server and multiple clients communicate using the TCP protocol.
- **Extendable**: The architecture allows easy addition of new protocols (like UDP, HTTP).
- **Stub for Testing**: A stub implementation is provided for unit testing the client without needing an active server.
- **Unit Tests**: Includes tests for client-server communication using the stub.

## Files Overview

- **`protocols.py`**: Contains an abstract base class `Protocol` that defines the communication methods.
- **`tcp_server.py`**: Implements a multi-threaded TCP server that handles incoming client connections.
- **`tcp_client.py`**: Implements the client that connects to the server and sends data.
- **`tcp_protocol.py`**: Implements the TCP protocol that is used for communication.
- **`test_sub.py`**: Contains unit tests for the client using a stub.

## How to Run
## For normal run 
Step 1 : python tcp_server.py
Step 2 : python tcp_client.py

## For Unit Testing
python -m unittest test_sub.py
