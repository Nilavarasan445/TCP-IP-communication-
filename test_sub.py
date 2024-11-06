import unittest
from tcp_client import TCPClient
from tcp_protocol import TCPProtocol 

class TestTCPClientStub(unittest.TestCase):

    def setUp(self):
        self.client = TCPClient(protocol=TCPProtocol(), use_stub=True)
        self.client.connect()

    def test_send_read_data(self):
        response = self.client.send_data("READ: Test data")
        self.assertEqual(response, "Stub response")
        print(f"Test Read Response: {response}")

    def test_send_write_data(self):
        response = self.client.send_data("WRITE: Test data")
        self.assertEqual(response, "Stub response")
        print(f"Test Write Response: {response}")

    def test_close_connection(self):
        self.client.close_connection()
        print("Connection closed with stub.")

if __name__ == "__main__":
    unittest.main()
