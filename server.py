from game import TicTacToeGame
from udp import UDP

class Controller:
    def __init__(self):
        # create server (IP, PORT)
        self.server = UDP("0.0.0.0", 12345)
        self.server.set_message_callback(self.process_message)  
        
        # Create game handler
        self.game = TicTacToeGame()

    def run(self):
        self.server.listen()
        self.game.run()
        

    def process_message(self, data, addr):
        print(f"Received message from {addr[0]}:{addr[1]}: {data}")
        
        if(data == "/reset"):
            self.game.handle_reset()
            print("Game reseted!")
        
        if(data == "/get"):
            stringToSend = ",".join(self.game.board)
            print(stringToSend)
            self.server.send_message(stringToSend, addr[0], addr[1])
            print("Game state sent!")
        

if __name__ == "__main__":
    
   controller = Controller()
   controller.run()