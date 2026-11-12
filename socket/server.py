from CompressioneBWT import BWT
import socket as sck

server = sck.socket(sck.AF_INET, sck.SOCK_STREAM)

IP = "127.0.0.1"
PORTA = 5000

with server:
    server.bind((IP, PORTA))

    server.listen()

    conn, addr = server.accept()

    with conn:

        messaggio = conn.recv(1024)
        print(messaggio)
        messaggio = BWT(messaggio)
        print(messaggio)

        conn.sendall(messaggio)