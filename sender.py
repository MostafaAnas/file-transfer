from tkinter import *	
from tkinter import filedialog
import socket  
import sys

  
# Function for opening the
# file explorer window
fname = ''
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/home",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
      
    # Change label contents
    label_file_explorer.configure(text="File Opened: "+filename)
    fname = filename
      
def sendFile(filename,s):
    try:
	    tosend_file = open(filename,'rb')
	    print('File opened')
    except Exception as fileerror:
	    print('Cannot open this file check this error: %s ' % str(fileerror))
    
    Filetosend = tosend_file.read(4096)
    while (Filetosend):
        print('Sending your file...')
        s.send(Filetosend)
        Filetosend = tosend_file.read(4096)
    tosend_file.close()
    print("File sended sucessfully")

def exit():
    s.close()
    sys.exit('Closed by User')



# Create the root window
window = Tk()
window.title("Sender")
# Set window size
window.geometry("800x400")

s = socket.socket() 
host = socket.gethostname()
port = 5000             
s.connect((host, port))



# Create a File Explorer label
label_file_explorer = Label(window, text = "File Explorer using Tkinter", width = 100, height = 4,fg = "blue")
button_explore = Button(window, text = "Browse Files", command = browseFiles)
button_exit = Button(window, text = "Exit",command = exit)
button_send = Button(window, text = "Send File", command = sendFile(fname,s))                    

label_file_explorer.grid(column = 1, row = 1)
button_explore.grid(column = 1, row = 2)
button_send.grid(column = 1,row = 3)
button_exit.grid(column = 1,row = 4)



window.mainloop()
