import asyncio
import websockets

class MessageType:
    DISCONNECT = "DISCONNECT"
    LETTER     = "LETTER"

class Server:

    def __init__(self, ip, port):
        self.server = websockets.serve(self.start_server, ip, port)

    async def start_server(self, sock, path):
        while True:
            packet = await sock.recv()

            if not packet:
                continue

            self.unpack_message(packet)
            print(f"[RECEIVED] {packet}")

    def unpack_message(self, packet):
        msg_type, msg = packet.split('$', 1)

        if (msg_type == MessageType.LETTER):
            pass
        else:
            print("[ERROR] Invalid message received of type: {msg_type}")

if __name__ == "__main__":
    morse_server = Server(IP, PORT)

