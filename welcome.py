import tkinter as tk
from PIL import ImageTk
from tkinter import messagebox
import os

root = tk.Tk()
root.attributes('-fullscreen', True)
canvas1=tk.Canvas(root,width=1280,height=720)
canvas1.pack()
logo=ImageTk.PhotoImage(file=r'welcome.png')

def call():
	os.system('python secondpage.py')
	global root
	root.destroy()

w=tk.Label(root,image=logo,width=1280,height=720)
button1=tk.Button(root,text='NEXT',bg='black',fg='yellow',command=call)
canvas1.create_window(640,350,window=w)
canvas1.create_window(1200,680,window=button1)

root.mainloop()

