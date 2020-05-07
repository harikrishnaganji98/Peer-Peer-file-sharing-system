# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 21:19:07 2019

@author: harik
"""

from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import socket
from threading import Thread
from socketserver import ThreadingMixIn
import webbrowser
i=0
TCP_IP = ''
TCP_PORT = 9001
BUFFER_SIZE = 9999999999

a=[]



from tkinter.filedialog import *
def open_file(): 
    filename = askopenfilename(initialdir = "/",title = "Select file",filetypes = (("all files","*.*"),("jpeg files","*.jpg")))
    aa=""
    for i in filename:
        if(i=="/"):
            aa=aa+"\\"
        else:
            aa=aa+i
    a.append(aa)

def send():
    if(a):
        root.destroy()
    else:
        w1 = tk.Label(root, text='SELECT ANY ONE FILE',fg="red") 
        w1.place(x=20,y=130)



def show():
    
    w = tk.Label(root, text='CONNECTED USERS')
    w.place(x=20,y=90)
    textBox=Text(root, height=2, width=40)
    textBox.pack()
    textBox.place(x=100,y=115)
    textBox.insert(tk.END,(ip,port))




class ClientThread(Thread):

    def __init__(self,ip,port,sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
#        print (" New thread started for "+ip+":"+str(port))
    

    def run(self):
        
        filename=a[0]
        f = open(filename,'rb')
        while True:
            l = f.read(BUFFER_SIZE)
            while (l):
                self.sock.send(l)
                #print('Sent ',repr(l))
                l = f.read(BUFFER_SIZE)
            if not l:
                f.close()
                self.sock.close()
                break

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))
threads = []

while True:
    tcpsock.listen(5)
    print ("Waiting for incoming connections...")
    (conn, (ip,port)) = tcpsock.accept()
    print ('Got connection from ', (ip,port))
    root = Tk() 
    root.geometry('200x200') 
    btn = Button(root, text ='CHOOSE FILE', command = lambda:open_file()) 
    btn.pack()
    btn.place(x=50,y=30) 
    btn1 = Button(root, text ='SEND', command = lambda:send()) 
    btn1.pack()
    btn1.place(x=65,y=90) 
    i=i+1
#    w = tk.Label(root, text='user - ')
    w1 = tk.Label(root, text=i)
#    w.place(x=20,y=110)
    w1.place(x=60,y=90)
#    w.pack()
    w1.pack()
    mainloop() 
    
    url = "http://"+ip+":8000/"
    webbrowser.open_new_tab(url)
#    root = tk.Tk()
#    button=Button(root, height=1, width=20, text="CONNECTED USERS", 
#                        command=lambda: show())
#    button.pack()
#    button.place(x=125,y=110)
#    root.title("SERVER")
#    root.geometry("400x300+100+100")
#    root.after(10000, lambda: root.destroy())
#    root.mainloop()
    newthread = ClientThread(ip,port,conn)
    newthread.start()
    threads.append(newthread)
   
for t in threads:
    t.join()
    

    

