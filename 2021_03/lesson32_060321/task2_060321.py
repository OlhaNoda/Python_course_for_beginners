# task2_060321
"""
Echo server with threading
Create a socket echo server which handles each connection in a separate Thread
"""
import socket
import threading


def create_serv_sock(host, port):
    serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_sock.bind((host, port))
    serv_sock.listen()
    return serv_sock


def accept_client_conn(serv_sock, client_id):
    client_sock, client_addr = serv_sock.accept()
    print(f'Client #{client_id} connected {client_addr}')
    return client_sock


def read_request(client_sock):
    try:
        while True:
            data = client_sock.recv(1024)
            if data:
                return data
            print('no data from', client_sock)
            return None
    except ConnectionResetError:
        return None


def handle_request(data):
    return data.upper()


def send_response(client_sock, response, client_id):
    client_sock.sendall(response)
    client_sock.close()
    print(f'Client #{client_id} has been served')


def run_server(host, port):
    serv_sock = create_serv_sock(host, port)
    client_id = 0
    while True:
        client_sock = accept_client_conn(serv_sock, client_id)
        t = threading.Thread(target=serve_client, args=(client_sock, client_id))
        t.start()
        client_id += 1


def serve_client(client_sock, client_id):
    request = read_request(client_sock)
    response = handle_request(request)
    send_response(client_sock, response, client_id)


if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 65432
    run_server(HOST, PORT)
