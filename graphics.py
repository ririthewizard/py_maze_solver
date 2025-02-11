from tkinter import *
from tkinter import ttk

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title("Maze Solver")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.protocol("WM_DELETE_WINDOW", self.close)

        self.canvas = Canvas(self.root, bg="white", width = self.width, height = self.height)
        self.canvas.grid(column=0, row=0, sticky=(N, W, E, S))

        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)


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

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point_a: Point, point_b: Point):
        self.point_a = point_a
        self.point_b = point_b

    def draw(self, canvas: Canvas, fill_color):
        canvas.create_line(self.point_a.x, self.point_a.y, self.point_b.x, self.point_b.y, fill=fill_color, width=2)
    

class Cell:
    def __init__(self, top_left_coord: Point, bottom_right_coord: Point, window=None):
        self.top_left_coord = top_left_coord
        self.bottom_right_coord = bottom_right_coord
        self.window = window
        self.walls = { 
                "left_wall": True,
                "top_wall": True,
                "right_wall": True,
                "bottom_wall": True}

    def __draw_cell(self, fill_color="black"):
        wall_coords = {
            "left_wall": (self.top_left_coord.x, self.top_left_coord.y,
                        self.top_left_coord.x, self.bottom_right_coord.y),
            "top_wall": (self.top_left_coord.x, self.top_left_coord.y,
                        self.bottom_right_coord.x, self.top_left_coord.y),
            "right_wall": (self.bottom_right_coord.x, self.top_left_coord.y,
                        self.bottom_right_coord.x, self.bottom_right_coord.y),
            "bottom_wall": (self.bottom_right_coord.x, self.bottom_right_coord.y,
                        self.top_left_coord.x, self.bottom_right_coord.y)
        }

        for wall_type, coords in wall_coords.items():
            if self.walls[wall_type]:
                line = Line(Point(coords[0], coords[1]), Point(coords[2], coords[3]))
                self.window.draw_line(line)
    
    def __find_center(self):
        return [int(((self.top_left_coord.x + self.bottom_right_coord.x) / 2)), int(((self.top_left_coord.y + self.bottom_right_coord.y) / 2))]

    def __draw_move(self, to_cell, undo=False):
        center_one = self.find_center()
        center_two = to_cell.find_center()
        line_between_centers = Line(Point(center_one[0], center_one[1]), Point(center_two[0], center_two[1]))

        if self.window:
            self.window.draw_line(line_between_centers, fill_color="red" if undo == False else "gray")
    
    def __repr__(self):
        return f"Cell(top_left={self.top_left_coord.x, self.top_left_coord.y}, bottom_right={self.bottom_right_coord.x, self.bottom_right_coord.y})"