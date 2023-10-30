import socket
import threading

class UDP:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.host, self.port))
        self.listening = True  # Flag to control the listening loop
        self.receive_thread = None  # Thread for receiving messages
        self.message_callback = None  # Callback function to process received messages

    def send_message(self, message, dest_host, dest_port):
        self.socket.sendto(message.encode(), (dest_host, dest_port))
    
    def receive_message(self, buffer_size=1024):
        data, addr = self.socket.recvfrom(buffer_size)
        return data.decode(), addr

    def listen(self, buffer_size=1024):
        def receive_loop():
            while self.listening:
                data, addr = self.receive_message(buffer_size)
                if self.message_callback:
                    self.message_callback(data, addr)

        self.listening = True
        self.receive_thread = threading.Thread(target=receive_loop)
        self.receive_thread.start()

    def set_message_callback(self, callback):
        self.message_callback = callback

    def stop_listening(self):
        self.listening = False
        if self.receive_thread:
            self.receive_thread.join()
        self.receive_thread = None

    def close(self):
        self.stop_listening()
        self.socket.close()

if __name__ == "__main__":
    server_host = "127.0.0.1"  # Use 0.0.0.0 to listen on all available network interfaces
    server_port = 12345  # Use any available port

    def process_message(data, addr):
        print(f"Received message from {addr[0]}:{addr[1]}: {data}")
        # You can process the received data here

    server = UDP(server_host, server_port)
    server.set_message_callback(process_message)  # Set the message processing callback
    server.listen()  # Start listening for commands

    input("Press Enter to stop listening...")

    server.stop_listening()
    server.close()
