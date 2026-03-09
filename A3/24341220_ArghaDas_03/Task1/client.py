# Task01 Client

import socket

HEADER=16
PORT=5173
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER, PORT)
FORMAT="utf8"
DISCONNECT_MSG="Task End."

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message=msg.encode(FORMAT)
    msg_length=len(message)
    send_length=str(msg_length).encode(FORMAT)
    send_length+=b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

# Get IP and Hostname
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

send(f"IP Address: {ip_address} And Device Name: {hostname}")
send(DISCONNECT_MSG)
