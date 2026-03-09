# Task01

import socket

HEADER=16
PORT=5173
SERVER=socket.gethostbyname(socket.gethostname())

#bind the address
ADDR=(SERVER, PORT) #binding IP and port
FORMAT="utf8"
DISCONNECT_MSG="Task End."

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM) # (ipv4, TCP)

server.bind(ADDR)


server.listen()
print("server is Listening")

conn, addr= server.accept()

connected=True

while connected: #client is connected
    msg_length=conn.recv(HEADER).decode(FORMAT)
    if msg_length:
        msg_length= int(msg_length)
        msg=conn.recv(msg_length).decode(FORMAT) # how many length of messages
        if msg==DISCONNECT_MSG:
            connected=False
            print("Goodbye")
            conn.send(DISCONNECT_MSG.encode(FORMAT))
        else:
            print(msg)
            conn.send("Message Received".encode(FORMAT))
conn.close()
