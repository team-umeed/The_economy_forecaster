import tkinter as tk
from PIL import ImageTk
from tkinter import messagebox
import os

root = tk.Tk()
root.attributes('-fullscreen', True)
canvas1=tk.Canvas(root,width=1280,height=720)
canvas1.pack()
logo = ImageTk.PhotoImage(file=r'carpet.png')
logo1 = ImageTk.PhotoImage(file=r'cer.png')
logo2 = ImageTk.PhotoImage(file=r'cocoa.png')
logo3 = ImageTk.PhotoImage(file=r'cro.png')
logo4 = ImageTk.PhotoImage(file=r'dairy.png')
logo5 = ImageTk.PhotoImage(file=r'emb.png')
logo6 = ImageTk.PhotoImage(file=r'inor.png')
logo7 = ImageTk.PhotoImage(file=r'medicinalplants.png')
logo8 = ImageTk.PhotoImage(file=r'milling.png')
logo9 = ImageTk.PhotoImage(file=r'ores.png')
logo10 = ImageTk.PhotoImage(file=r'paper.png')
logo11= ImageTk.PhotoImage(file=r'pharma.png')
logo12= ImageTk.PhotoImage(file=r'soap.png')
logo13= ImageTk.PhotoImage(file=r'stones.png')
logo14=ImageTk.PhotoImage(file=r'sugar.png')
logo15= ImageTk.PhotoImage(file=r'trees.png')
def call1():

	os.system('python carpets1.py')
	root.destroy()
def call2():

	os.system('python ceramics1.py')
	root.destroy()
def call3():

	os.system('python cocoa1.py')
	root.destroy()
def call4():

	os.system('python knittedfabrics1.py')
	root.destroy()
def call5():

	os.system('python dairy1.py')
	root.destroy()
def call6():

	os.system('python woven1.py')
	root.destroy()
def call7():

	os.system('python inorganic1.py')
	root.destroy()
def call8():

	os.system('python oilseeds1.py')
	root.destroy()
def call9():

	os.system('python milling1.py')
	root.destroy()
def call10():

	os.system('python ores1.py')
	root.destroy()
def call11():

	os.system('python paper1.py')
	root.destroy()
def call12():

	os.system('python pharma1.py')
	root.destroy()
def call13():

	os.system('python soaps1.py')
	root.destroy()
def call14():

	os.system('python salts1.py')
	root.destroy()
def call15():

	os.system('python sugar1.py')
	root.destroy()
def call16():

	os.system('python livetrees1.py')
	root.destroy()
def call():
	pass
def ExitApplication():
    root.destroy()

def callx():

	os.system('python welcome.py')
	root.destroy()


    



logox=ImageTk.PhotoImage(file=r'theme.png')
w0=tk.Label(root,image=logox,width=1280,height=720)
canvas1.create_window(640,350,window=w0)
HOME = tk.Button (root,text='HOME',command=callx,bg='blue',fg='white')
canvas1.create_window(100, 40, window=HOME)
buttonE = tk.Button (root,text='EXIT',command=ExitApplication,bg='blue',fg='white')
canvas1.create_window(1250, 50, window=buttonE)

w = tk.Label(root,image=logo,height=150,width=150)
button1 = tk.Button (root, text='CARPET',command=call1,bg='white',fg='black')

w1 = tk.Label(root,image=logo1,height=150,width=150)
button2 = tk.Button (root, text='CERAMICS',command=call2,bg='white',fg='black')

w2 = tk.Label(root,image=logo2,height=150,width=150)
button3 = tk.Button (root, text='COCOA',command=call3,bg='white',fg='black')

w3 = tk.Label(root,image=logo3,height=150,width=150)
button4 = tk.Button (root, text='CROTCHETED MATERIALS',command=call4,bg='white',fg='black')

w4 = tk.Label(root,image=logo4,height=150,width=150)
button5 = tk.Button (root, text='DAIRY PRODUCTS',command=call5,bg='white',fg='black')

w5 = tk.Label(root,image=logo5,height=150,width=150)
button6 = tk.Button (root, text='EMBROIDERY WORKS',command=call6,bg='white',fg='black')

w6 = tk.Label(root,image=logo6,height=150,width=150)
button7 = tk.Button (root, text='INORGANIC CHEMICALS',command=call7,bg='white',fg='black')

w7 = tk.Label(root,image=logo7,height=150,width=150)
button8 = tk.Button (root, text='MEDICINAL PLANTS',command=call8,bg='white',fg='black')

w8 = tk.Label(root,image=logo8,height=150,width=150)
button9 = tk.Button (root, text='MILLING PRODUCTS',command=call9,bg='white',fg='black')

w9 = tk.Label(root,image=logo9,height=150,width=150)
button10 = tk.Button (root, text='ORES',command=call10,bg='white',fg='black')

w10 = tk.Label(root,image=logo10,height=150,width=150)
button11 = tk.Button (root, text='PAPER INDUSTRY',command=call11,bg='white',fg='black')

w11 = tk.Label(root,image=logo11,height=150,width=150)
button12 = tk.Button (root, text='PHARMACEUTICAL INDUSTRIES',command=call12,bg='white',fg='black')

w12 = tk.Label(root,image=logo12,height=150,width=150)
button13 = tk.Button (root, text='SOAPS',command=call13,bg='white',fg='black')

w13 = tk.Label(root,image=logo13,height=150,width=150)
button14 = tk.Button (root, text='EARTH STONES',command=call14,bg='white',fg='black')

w14 = tk.Label(root,image=logo14,height=150,width=150)
button15 = tk.Button (root, text='SUGAR AND PRODUCE',command=call15,bg='white',fg='black')

w15 = tk.Label(root,image=logo15,height=150,width=150)
button16 = tk.Button (root, text='RARE TREES',command=call16,bg='white',fg='black')

button0 = tk.Button (root, text='CHOOSE THE FIELD YOU WANT TO SEE',command=call,bg='white',fg='red')

canvas1.create_window(640, 30, window=button0)

canvas1.create_window(620, 150, window=w)
canvas1.create_window(620, 150, window=button1)

canvas1.create_window(620, 300, window=w1)
canvas1.create_window(620, 300, window=button2)

canvas1.create_window(620, 450, window=w2)
canvas1.create_window(620, 450, window=button3)

canvas1.create_window(620, 600, window=w11)
canvas1.create_window(620, 600, window=button12)

canvas1.create_window(350, 150, window=w3)
canvas1.create_window(350, 250, window=button4)

canvas1.create_window(350, 360, window=w4)
canvas1.create_window(350, 440, window=button5)

canvas1.create_window(350, 570, window=w5)
canvas1.create_window(350, 670, window=button6)

canvas1.create_window(150, 150, window=w12)
canvas1.create_window(150, 250, window=button13)

canvas1.create_window(890, 150, window=w6)
canvas1.create_window(890, 250, window=button7)

canvas1.create_window(890, 360, window=w7)
canvas1.create_window(890, 440, window=button8)

canvas1.create_window(890, 570, window=w8)
canvas1.create_window(890, 670, window=button9)

canvas1.create_window(150, 360, window=w13)
canvas1.create_window(150, 440, window=button14)

canvas1.create_window(1100, 150, window=w9)
canvas1.create_window(1100, 250, window=button10)

canvas1.create_window(1100, 360, window=w10)
canvas1.create_window(1100, 440, window=button11)

canvas1.create_window(150, 570, window=w14)
canvas1.create_window(150, 670, window=button15)

canvas1.create_window(1100, 570, window=w15)
canvas1.create_window(1100, 670, window=button16)


root.mainloop()

