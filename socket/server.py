import socket as sck

server = sck.socket(sck.AF_INET, sck.SOCK_STREAM)

IP = "127.0.0.1"
PORTA = 5000

server.bind()