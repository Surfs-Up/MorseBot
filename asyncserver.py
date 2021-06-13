import asyncio
import websockets

SERVER = "localhost"
PORT = 5050

class Server:

    def __init__(self, server, port):
        self.server = websockets.serve(self.start_server, server, port)

        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.server)
        loop.run_forever()

    async def start_server(self, sock, path):
        while True:
            packet = await sock.recv()
            print(f"received message {packet}")
            await sock.send("message received")

if __name__ == "__main__":
    morse_server = Server(SERVER, PORT)

