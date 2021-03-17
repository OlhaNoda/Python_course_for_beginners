import socket
import threading


class Server:
    def __init__(self, host, port):
        self.clients = {}
        self.host = host
        self.port = port

    def serv_socket(self):
        serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serv_sock.bind((self.host, self.port))
        serv_sock.listen(5)
        print(f"Сервер запущен {self.host} : {self.port}")
        return serv_sock

    def run(self):
        while True:
            connection, address = self.serv_socket().accept()
            client_name = connection.recv(1024)
            client_name = client_name.decode()
            self.clients[client_name] = connection
            threading.Thread(target=self.receive_message, args=(connection, client_name)).start()

    def receive_message(self, connection, client_name):
        try:
            while True:
                msg = connection.recv(1024)
                if msg:
                    self.send_message(msg, client_name)
                else:
                    break
        finally:
            connection.close()
            del (self.clients[client_name])

    def send_message(self, message, sender):
        if self.clients:
            for client_name in self.clients:
                if client_name != sender:
                    msg = f'{sender}: {message.decode()}'
                    self.clients[client_name].send(msg.encode())


if __name__ == "__main__":
    chat_host = '127.0.0.1'
    chat_port = 65432
    chat_server = Server(chat_host, chat_port)
    chat_server.run()
