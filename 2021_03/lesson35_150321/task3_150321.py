#task3_150321
"""
Echo server with asyncio
Create a socket echo server which handles each connection using asyncio Tasks.
"""

import socket
import asyncio


def create_serv_sock(host, port):
    serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_sock.bind((host, port))
    serv_sock.listen()
    return serv_sock


def accept_client_conn(serv_sock):
    client_sock, client_addr = serv_sock.accept()
    print(f'Client #{client_addr} connected')
    return client_sock


def read_request(client_sock):
    try:
        data = client_sock.recv(1024)
        if data:
            return data
        print('no data from', client_sock)
        return None
    except ConnectionResetError:
        return None


def handle_request(data):
    return data.upper()


def send_response(client_sock, response):
    client_sock.sendall(response)


async def run_server(host, port):
    serv_sock = create_serv_sock(host, port)
    while True:
        client_sock = accept_client_conn(serv_sock)
        task = asyncio.create_task(server_client(client_sock))
        await task


async def server_client(client_sock):
    request = read_request(client_sock)
    response = handle_request(request)
    send_response(client_sock, response)


if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 65432
    loop = asyncio.get_event_loop()
    run = loop.run_until_complete(run_server(HOST, PORT))
