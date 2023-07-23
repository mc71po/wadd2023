from tkinter import Tk, Canvas
frame=Tk()
canvas=Canvas(bg='black',height=400,width=400)
 
canvas.create_rectangle(50, 60, 240, 160, fill='yellow', outline='blue')
canvas.create_text(100, 100, text='Mark NG SHI HIN', anchor='nw', font='TkMenuFont', fill='black')
canvas.create_line(100, 115, 195, 115)
canvas.pack()
