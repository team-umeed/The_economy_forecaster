import tkinter as tk
from PIL import ImageTk,Image
from tkinter import messagebox
import os
import webbrowser

root=tk.Tk()
root.attributes('-fullscreen', True)
canvas1=tk.Canvas(root,width=1280,height=720)
canvas1.pack()
logo=ImageTk.PhotoImage(file=r'2nd page.png')


def call1():
	os.system('python farmingpage.py')
	root.destroy()
def call2():
	os.system('python primary.py')
	root.destroy()

def ExitApplication():
    root.destroy()

def callx():
	os.system('python welcome.py')
	root.destroy()
def callback():
	webbrowser.open_new('https://umeedeconomyforecaster.000webhostapp.com/')
	root.destroy()


    


w=tk.Label(root,image=logo,width=1280,height=720)
HOME = tk.Button (root,text='HOME',command=callx,bg='blue',fg='white')
canvas1.create_window(100, 40, window=HOME)
buttonE = tk.Button (root,text='EXIT',command=ExitApplication,bg='blue',fg='white')
buttonw=tk.Button (root,text='Visit our Website \n and check our bot',command=callback,bg='blue',fg='white')
canvas1.create_window(1250, 50, window=buttonE)
w2=tk.Label(root, text='PRIMARY INDUSTRIES')
w3=tk.Label(root,text='FARMING')
img1=ImageTk.PhotoImage(Image.open(r'farm.png'))
img2=ImageTk.PhotoImage(Image.open(r'Industries.png'))
button1=tk.Button(root,image=img1,bg='black',fg='yellow',command=call1,height=220,width=220)
button2=tk.Button(root,image=img2,bg='black',fg='yellow',command=call2,height=220,width=220)
canvas1.create_window(500,350,window=button1)
canvas1.create_window(500,500,window=w3)
canvas1.create_window(640,350,window=w)
canvas1.create_window(750,500,window=w2)
canvas1.create_window(750,350,window=button2)
canvas1.create_window(100,100,window=buttonw)



root.mainloop()
