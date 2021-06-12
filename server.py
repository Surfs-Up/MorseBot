import socket
import threading

PACKETSIZE = 64
# SERVER = "192.168.1.55"
SERVER = "127.0.0.1"
PORT = 5050
FORMAT = 'utf-8'

class Server:

    serversock = None

    def __init__(self, server, port):
        self.serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serversock.bind((server,port))

    def handle_client(self, conn, addr):
        print(f"[NEW CONNECTION] {addr} connected.")

        connected = True
        while connected:

            msg = conn.recv(PACKETSIZE).decode(FORMAT)

            if not msg:
                continue

            print(f"[{addr}] {msg}")

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

server = Server(SERVER, PORT)
server.start_server()

