import socket
import sys
import pickle

## Definición de la clase Mensaje ##
class Mensaje:
    emoji =""
    text = ""
## Definición de la clase Mensaje ##

s = socket.socket()                                                 #Crear socket
host = input(str("Please enter the hostname of the server : "))
port = 8080
s.connect((host,port))                                              #vincular
name = input(str("Please enter your username : "))
print(" Connected to chat server")

s.send(name.encode())                   
s_name = s.recv(1024)                                               #Recibir el nombre de usario del servidor
s_name = s_name.decode()
print("")
print(s_name, "has joined the chat room ")

while 1:
    mensaje = Mensaje()                                         #definir mensaje de clase Mensaje
    data = s.recv(4096)
    data_variable = pickle.loads(data)                          #Des-serializar el flujo de datos
    print(s_name, ":" ,data_variable.emoji,data_variable.text)  #Imprimir los parámetros emoji y text de la variable data_variable
    print("")
    mensaje = Mensaje()
    mensaje.emoji=  input(str("Please enter your emoji: "))     #recibir parámetros
    mensaje.text =  input(str("Please enter your text "))
    message = pickle.dumps(mensaje)                             #Serializar jerarquía de objetos
    s.send(message)
    print("")

