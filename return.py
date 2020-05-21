import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk,Image
root=tk.Tk()
canvas1 = tk.Canvas(root, width = 1280, height = 720)
canvas1.pack()

def ExitApplication1():
    tk.messagebox.showinfo('Return','YOU WILL BE GUIDED TO MAIN SCREEN')

buttonR = tk.Button (root,text='RETURN',command=ExitApplication1,bg='blue',fg='white')
canvas1.create_window(1250,700,window = buttonR)

root.mainloop()


    
