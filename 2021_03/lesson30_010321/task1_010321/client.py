# task1_010321
"""
During the lesson, we have created a server and client, which use TCP/IP protocol for communication via sockets.
In this task, you have to create a server and client, which will use user datagram protocol (UDP) for communication.
"""

import socket

HOST = '127.0.0.1'
PORT = 65432

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = input('Enter message to send: ')
client_socket.sendto(data.encode('utf-8'), (HOST, PORT))
data = client_socket.recvfrom(1024)
reply = data[0]
print('Server reply: ' + reply.decode('utf-8'))
client_socket.close()
