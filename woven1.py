import tkinter as tk
from PIL import ImageTk
from tkinter import messagebox
import os

root = tk.Tk()
root.attributes('-fullscreen', True)
canvas1=tk.Canvas(root,width=1280,height=720)
canvas1.pack()
logo=ImageTk.PhotoImage(file=r'woven1.png')

def call():
	os.system('python woven.py')
    
def ExitApplication():
    root.destroy()

def call1():
	os.system('python welcome.py')
	root.destroy()


    
w=tk.Label(root,image=logo,width=1280,height=720)
HOME = tk.Button (root,text='HOME',command=call1,bg='blue',fg='white')
canvas1.create_window(100, 40, window=HOME)
buttonE = tk.Button (root,text='EXIT',command=ExitApplication,bg='blue',fg='white')
canvas1.create_window(1250, 50, window=buttonE)
button1=tk.Button(root,text='GRAPH',bg='black',fg='yellow',command=call)
canvas1.create_window(640,350,window=w)
canvas1.create_window(1200,680,window=button1)

root.mainloop()

