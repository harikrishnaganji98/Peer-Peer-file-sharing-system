import socket
import time
import webbrowser
start = time.process_time()
ip='10.1.133.155'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
s.connect((ip, 9001))
def transfer():
#    inputValue=textBox.get("1.0",'end-1c')
    fn=textBox1.get("1.0",'end-1c')
#    print(inputValue1)
    f = open(fn, "wb")
    file_data=s.recv(9999999999)
    f.write(file_data)
    f.close()
    print("Done receiving")
    ww = tk.Label(root, text='FILE RECIEVED',fg="green") 
    ww.place(x=20,y=190)
    
import tkinter as tk
from tkinter import *
  

root = tk.Tk()
#w = tk.Label(root, text='ENTER IP-ADDRESS')
#w.place(x=20,y=90)
w1 = tk.Label(root, text='NAME FOR RECIEVED FILE \nWITH EXTENSION')
 
w1.place(x=20,y=130)
root.title("FILE SHARE")

#textBox=Text(root, height=1, width=40)
#textBox.pack()
#textBox.place(x=165,y=88)
textBox1=Text(root, height=1, width=40)
textBox1.pack()
textBox1.place(x=165,y=127)
buttonCommit=Button(root, height=1, width=10, text="SAVE AS", 
                    command=lambda: transfer())
buttonCommit.pack()
buttonCommit.place(x=110,y=180)
root.geometry("400x300+100+100")
root.mainloop()
#url = "http://"+ip+":8000/"
#webbrowser.open_new_tab(url)
#print(time.process_time() - start)