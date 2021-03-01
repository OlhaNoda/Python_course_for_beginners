import socket
from caesar_cipher import caesar

HOST = '127.0.0.1'
PORT = 65432

sock = socket.socket()
sock.bind((HOST, PORT))
sock.listen(1)
conn, addr = sock.accept()
while True:
    data = conn.recv(1024)
    if not data:
        break
    data = caesar(data.decode()).encode()
    conn.send(data)

conn.close()
