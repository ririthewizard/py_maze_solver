from tkinter import *
from tkinter import ttk

def save_posn(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y

def add_line(event):
    canvas.create_line((lastx, lasty, event.x, event.y))
    save_posn(event)

root = Tk()
root.title("Balls")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

canvas = Canvas(root)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))
canvas.bind("<1>", save_posn)
canvas.bind("<B1-Motion>", add_line)

root.mainloop()
