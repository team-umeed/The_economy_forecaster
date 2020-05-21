import tkinter as tk
from PIL import ImageTk
from tkinter import messagebox
import os

root = tk.Tk()
root.attributes('-fullscreen', True)
canvas1=tk.Canvas(root,width=1280,height=720)
canvas1.pack()
logo55=ImageTk.PhotoImage(file=r'theme.png')
logo = ImageTk.PhotoImage(file=r'livestock.png')
logo1 = ImageTk.PhotoImage(file=r'fruit.png')
logo2 = ImageTk.PhotoImage(file=r'coffee.png')
logo3 = ImageTk.PhotoImage(file=r'cereals.png')
logo4 = ImageTk.PhotoImage(file=r'silk.png')
logo5 = ImageTk.PhotoImage(file=r'cotton.png')
logo6 = ImageTk.PhotoImage(file=r'wool.png')
logo7 = ImageTk.PhotoImage(file=r'animalfat.png')
logo8 = ImageTk.PhotoImage(file=r'rubber.png')

def call():

	os.system('python liveanimals1.py')
	root.destroy()
def call1():

	os.system('python ediblefruit1.py')
	root.destroy()
def call2():

	os.system('python coffee1.py')
	root.destroy()
def call3():

	os.system('python cereals1.py')
	root.destroy()
def call4():

	os.system('python silk1.py')
	root.destroy()
def call5():

	os.system('python cotton1.py')
	root.destroy()
def call6():

	os.system('python wool1.py')
	root.destroy()
def call7():

	os.system('python animalfat1.py')
	root.destroy()
def call8():

	os.system('python rubber1.py')
	root.destroy()



def ExitApplication():
    root.destroy()

def callx():

	os.system('python welcome.py')
	root.destroy()


    



w55=tk.Label(root,image=logo55,width=1280,height=720)
w = tk.Label(root,image=logo,height=200,width=200)
HOME = tk.Button (root,text='HOME',command=callx,bg='blue',fg='white')
canvas1.create_window(100, 40, window=HOME)
buttonE = tk.Button (root,text='EXIT',command=ExitApplication,bg='blue',fg='white')
canvas1.create_window(1250, 50, window=buttonE)
button1 = tk.Button (root, text='LIVESTOCK',command=call,bg='black',fg='white')
w1 = tk.Label(root,image=logo1,height=200,width=200)
button2 = tk.Button (root, text='VEGETABLES',command=call1,bg='black',fg='white')
w2 = tk.Label(root,image=logo2,height=200,width=200)
button3 = tk.Button (root, text='COFFEE',command=call2,bg='black',fg='white')
w3 = tk.Label(root,image=logo3,height=200,width=200)
button4 = tk.Button (root, text='CEREALS',command=call3,bg='black',fg='white')
w4 = tk.Label(root,image=logo4,height=200,width=200)
button5 = tk.Button (root, text='SILK',command=call4,bg='black',fg='white')
w5 = tk.Label(root,image=logo5,height=200,width=200)
button6 = tk.Button (root, text='COTTON',command=call5,bg='black',fg='white')
w6 = tk.Label(root,image=logo6,height=200,width=200)
button7 = tk.Button (root, text='WOOLEN MATERIALS',command=call6,bg='black',fg='white')
w7 = tk.Label(root,image=logo7,height=200,width=200)
button8 = tk.Button (root, text='ANIMAL FATS',command=call7,bg='black',fg='white')
w8 = tk.Label(root,image=logo8,height=200,width=200)
button9 = tk.Button (root, text='RUBBER',command=call8,bg='black',fg='white')

canvas1.create_window(640,360, window=w55)
canvas1.create_window(350, 150, window=w)
canvas1.create_window(350, 250, window=button1)
canvas1.create_window(350, 360, window=w1)
canvas1.create_window(350, 440, window=button2)
canvas1.create_window(350, 570, window=w2)
canvas1.create_window(350, 670, window=button3)
canvas1.create_window(620, 150, window=w3)
canvas1.create_window(620, 250, window=button4)
canvas1.create_window(620, 360, window=w4)
canvas1.create_window(620, 440, window=button5)
canvas1.create_window(620, 570, window=w5)
canvas1.create_window(620, 670, window=button6)
canvas1.create_window(890, 150, window=w6)
canvas1.create_window(890, 250, window=button7)
canvas1.create_window(890, 360, window=w7)
canvas1.create_window(890, 440, window=button8)
canvas1.create_window(890, 570, window=w8)
canvas1.create_window(890, 670, window=button9)



root.mainloop()

root.mainloop()
