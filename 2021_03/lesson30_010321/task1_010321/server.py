# task1_010321
"""
During the lesson, we have created a server and client, which use TCP/IP protocol for communication via sockets.
In this task, you have to create a server and client, which will use user datagram protocol (UDP) for communication.
"""

import socket

HOST = '127.0.0.1'
PORT = 65432

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind((HOST, PORT))
while True:
    question = input('Do you want to quit? y\\n: ')
    if question == 'y':
        break
    print('wait data...')
    conn, addr = udp_socket.recvfrom(1024)
    print('client addr: ', addr)
    udp_socket.sendto(b'message received by the server', addr)
udp_socket.close()
