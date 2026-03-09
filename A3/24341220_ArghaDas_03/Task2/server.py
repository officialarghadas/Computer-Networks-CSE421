# Task02

import socket

HEADER=16
PORT=5174
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
            vowels = "aeiouAEIOU"
            count = 0
            for i in msg:
                if i in vowels:
                    count += 1
            if count == 0:
                conn.send("Not enough vowels".encode(FORMAT))
            elif count <= 2:
                conn.send("Enough vowels I guess".encode(FORMAT))
            else:
                conn.send("Too many vowels".encode(FORMAT))
conn.close()
