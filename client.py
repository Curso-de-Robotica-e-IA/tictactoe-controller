import socket

class UDPClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def send_message(self, message):
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.sendto(message.encode(), (self.host, self.port))
        udp_socket.close()

if __name__ == "__main__":
    server_host = "127.0.0.1"  # Replace with the IP address where the server is running
    server_port = 12345  # Use the same port as the server

    client = UDPClient(server_host, server_port)

    while True:
        message = input("Enter a message to send (or type 'exit' to quit): ")
        if message == "exit":
            break
        client.send_message(message)

    print("Client program exited.")
