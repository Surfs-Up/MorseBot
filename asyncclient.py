import asyncio
import websockets

class Client:

    def __init__(self, connection_string):
        self.connection_string = connection_string

        asyncio.get_event_loop().run_until_complete(self.start_client())

    async def start_client(self):
        async with websockets.connect(self.connection_string) as sock:
            while True:
                packet = input("enter message")
                await sock.send(packet)
                print(await sock.recv())

if __name__ == "__main__":
    morse_client = Client("ws://localhost:5050")
