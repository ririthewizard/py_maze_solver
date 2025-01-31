from tkinter import *
from tkinter import ttk

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Solver")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.protocol("WM_DELETE_WINDOW", self.close)

        self.canvas = Canvas(self.root, bg="white", height=height, width=width)
        self.canvas.grid(column=0, row=0, sticky=(N, W, E, S))

        self.running = False

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print("Window closed...")

    def close(self):
        self.running = False

    
def main():
    win = Window(800, 600)
    win.wait_for_close()

main()