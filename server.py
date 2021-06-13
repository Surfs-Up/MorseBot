import socket
import threading
import asyncio

PACKETSIZE = 64
SERVER = "192.168.1.55"
PORT = 5050
FORMAT = 'utf-8'

class MessageType:
    DISCONNECT = "DISCONNECT"
    LETTER     = "LETTER"

class Server:

    serversock = None

    def __init__(self, bot):
        self.serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serversock.bind((SERVER,PORT))
        self.bot = bot

    def handle_client(self, conn, addr):
        print(f"[NEW CONNECTION] {addr} connected.")

        connected = True
        while connected:

            packet = conn.recv(PACKETSIZE).decode(FORMAT)

            if not packet:
                continue

            self.unpack_message(packet)

            print(f"[{addr}] {packet}")

        conn.close()

    def start_server(self):
        print("[STARTING] server is starting...")
        self.serversock.listen()
        print(f"[LISTENING] Server is listening on {SERVER}")

        while True:
            conn, addr = self.serversock.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn,addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.activeCount() -1}")

    def unpack_message(self, packet):
        msg_type, msg = packet.split('$', 1)

        if (msg_type == MessageType.LETTER):
            print(f"recieved letter {msg}")
            self.bot.send_letter(msg)
        else:
            print("[ERROR] Invalid message received of type: {msg_type}")

