from tkinter import *
import sys
import socket

window = Tk()
window.title("Receiver")

s = socket.socket()         
host = socket.gethostname() 
port = 5000
s.bind((host, port))


recv_file = open('filename.ext','wb')
s.listen(5)          
while True:
    c, addr = s.accept() 
    print('File will recv from: ', addr)
    print('Start recv...')
    FILETORECV = c.recv(4096)
    while (FILETORECV):
        print("Receiving...")
        recv_file.write(FILETORECV)
        FILETORECV = c.recv(4096)
    recv_file.close()
    print("File recv or converted sucessfully.")
    c.send(b'Message from client: File received sucessfully. tnx')
c.close()
sys.exit('closed by system')