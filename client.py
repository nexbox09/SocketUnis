import socket
import sys
import pickle
import time
import random
from datetime import datetime
from typing import final

## Definición de la clase Mensaje ##
class IDP:
    callingPartyNumber =""
    mscAddress = ""
    calledPartyNumber = ""
## Definición de la clase Mensaje ##

class Cue:
    continuar = ""

class RRB:
    o_answer = bool
    o_disc = bool

class ERB:
    o_answer = bool
    o_disc = bool

class ACH:
    tiempo = int

class ACR:
    tiempo = int

s = socket.socket()                                                 #Crear socket
host = input(str("Please enter the mscAddress : "))
port = 8080
s.connect((host,port))                                              #vincular
name = input(str("Please enter your username : "))
print(" Connected to the central")

s.send(name.encode())                   
s_name = s.recv(1024)                                               #Recibir el nombre de usario del servidor
s_name = s_name.decode()
print("")
print(s_name, "has joined the chat room ")
tiempoacr = 0

while 1:
    mensaje = IDP()          
    mensaje.callingPartyNumber =  "3506013309"              #recibir parámetros
    mensaje.mscAddress =  "91655340000512"   
    mensaje.calledPartyNumber =  "3144582356"  
    message = pickle.dumps(mensaje)   
    s.send(message)
    print("IDP enviado")
    print("")                                     #definir mensaje de clase Mensaje
    data = s.recv(4096)
    data_variable = pickle.loads(data)                          #Des-serializar el flujo de datos
    print(s_name, ":" ,data_variable.continuar)  #Imprimir los parámetros emoji y text de la variable data_variable
    print("")
    
    data = s.recv(4096)
    data_variable = pickle.loads(data)                          #Des-serializar el flujo de datos
    print(s_name, ":" ,data_variable.o_answer,data_variable.o_disc)  #Imprimir los parámetros emoji y text de la variable data_variable
    print("RRB recibido")
    print("")
    time.sleep(random.randint(1,10))
    erb = ERB()
    erb.o_answer = True
    erb.o_disc = False
    erb = pickle.dumps(erb)  
    inicio = datetime.now()
    s.send(erb) 
    print("ERB enviado (o_answer)", inicio)
    print("")

    data = s.recv(4096)
    data_variable = pickle.loads(data)
    time.sleep(data_variable.tiempo)   
    tiempoacr = data_variable.tiempo                      
    print("ACR(",tiempoacr,")")
    print("")
    data = s.recv(4096)
    data_variable = pickle.loads(data)
    time.sleep(data_variable.tiempo)   
    tiempoacr = tiempoacr + data_variable.tiempo                      
    print("ACR(",tiempoacr,")")
    print("")
    data = s.recv(4096)
    data_variable = pickle.loads(data)
    time.sleep(data_variable.tiempo)   
    tiempoacr = tiempoacr + data_variable.tiempo                      
    print("ACR(",tiempoacr,")")
    print("")

    erb = ERB()
    erb.o_answer = False
    erb.o_disc = True
    erb = pickle.dumps(erb)  
    finalizacion = datetime.now()
    s.send(erb) 
    print("ERB enviado (o_disc) ", finalizacion)
    print("Llamada finalizada")
    print("Duracion:", finalizacion - inicio)
    print("")

    exit()