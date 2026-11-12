import socket as sck

client = sck.socket(sck.AF_INET, sck.SOCK_STREAM)

IP = "127.0.0.1"
PORTA = 5000

with client:
    client.connect((IP, PORTA))

    messaggio = input("Inserisci un messaggio:")

    client.sendall(messaggio.encode())
    
    risposta = client.recv(1024)
    print("Risposta del server:", risposta.decode())