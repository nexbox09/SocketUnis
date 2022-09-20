import socket
import sys
import pickle

class Mensaje:
    emoji =""
    text = ""

s = socket.socket()
host = input(str("Please enter the hostname of the server : "))
port = 8080
s.connect((host,port))
name = input(str("Please enter your username : "))
print(" Connected to chat server")

s.send(name.encode())
s_name = s.recv(1024)
s_name = s_name.decode()
print("")
print(s_name, "has joined the chat room ")

while 1:
    mensaje = Mensaje()
    data = s.recv(4096)
    data_variable = pickle.loads(data)
    print(s_name, ":" ,data_variable.emoji,data_variable.text)
    print("")
    mensaje = Mensaje()
    mensaje.emoji=  input(str("Please enter your emoji: "))
    mensaje.text =  input(str("Please enter your text "))
    message = pickle.dumps(mensaje)
    s.send(message)
    print("")

