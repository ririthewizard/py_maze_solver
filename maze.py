from tkinter import *
from tkinter import ttk
from graphics import *
import time

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None
    ):
        self.x1, self.y1, self.num_rows, self.num_cols, self.cell_size_x, self.cell_size_y, self.win = x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win
        self._create_cells()
    
    def _create_cells(self):
        self.cells = []
        for cols in range(self.num_cols):
            self.cells.append([])
            for rows in range(self.num_rows):
                self.cells[cols].append(Cell(Point((self.x1 + (self.cell_size_x * cols)), (self.y1 + (self.cell_size_y * rows))), 
                                                        Point((self.x1 + (self.cell_size_x * cols) + self.cell_size_x), (self.y1 + (self.cell_size_y * rows) + self.cell_size_y)), self.win))
                self._draw_cell(cols, rows)
        
    def _draw_cell(self, i, j):
        cell_position = self.cells[i][j]
        temp_cell = Cell(Point(cell_position.top_left_coord.x, cell_position.top_left_coord.y), 
                        Point(cell_position.bottom_right_coord.x, cell_position.bottom_right_coord.y))
        temp_cell._Cell__draw_cell()
        #current_cell = self.cells[i][j]
        #current_cell._Cell__draw
        self._animate()
    
    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)