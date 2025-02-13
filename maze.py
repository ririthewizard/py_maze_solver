from tkinter import *
from tkinter import ttk
from graphics import *
import time
import random

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None,
            ):
        self.x1, self.y1, self.num_rows, self.num_cols, self.cell_size_x, self.cell_size_y, self.win, = x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win 
        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

    def _create_cells(self):
        self.cells = []
        for cols in range(self.num_cols):
            self.cells.append([])
            for rows in range(self.num_rows):
                self.cells[cols].append(Cell(Point((self.x1 + (self.cell_size_x * cols)), (self.y1 + (self.cell_size_y * rows))), 
                                             Point((self.x1 + (self.cell_size_x * cols) + self.cell_size_x), (self.y1 + (self.cell_size_y * rows) + self.cell_size_y)), self.win))
                if self.win:
                    self._draw_cell(cols, rows)

    def _draw_cell(self, i, j):
        current_cell = self.cells[i][j]
        current_cell._Cell__draw_cell()
        self._animate()

    def _animate(self):
        if self.win:
            self.win.redraw()
            time.sleep(0.03)

    def _break_entrance_and_exit(self):
        self.cells[0][0].walls["top_wall"] = False
        self._draw_cell(0, 0)
        self.cells[self.num_cols - 1][self.num_rows - 1].walls["bottom_wall"] = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)

    def _break_walls_r(self, i, j):
        self.cells[i][j].visited = True 
        while True:
            to_visit = []

            #i = cols j = rows
            #left
            if (i - 1 >= 0) and self.cells[i - 1][j].visited == False:
                to_visit.append((i - 1, j))
            #up
            if (j - 1 >= 0) and self.cells[i][j - 1].visited == False:
                to_visit.append((i, j - 1))
            #right
            if (i < self.num_cols - 1) and self.cells[i + 1][j].visited == False:
                to_visit.append((i + 1, j))
            #down
            if (j < self.num_rows - 1) and self.cells[i][j + 1].visited == False:
                to_visit.append((i, j + 1))

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return

            dest_coords = to_visit[random.randint(0, len(to_visit) - 1)]
            
            if dest_coords[0] < i:
                self.cells[i][j].walls["left_wall"] = False
                self.cells[i - 1][j].walls["right_wall"] = False
            if dest_coords[1] < j:
                self.cells[i][j].walls["top_wall"] = False
                self.cells[i][j - 1].walls["bottom_wall"] = False
            if dest_coords[0] > i:
                self.cells[i][j].walls["right_wall"] = False
                self.cells[i + 1][j].walls["left_wall"] = False
            if dest_coords[1] > j:
                self.cells[i][j].walls["bottom_wall"] = False
                self.cells[i][j + 1].walls["top_wall"] = False

            self._break_walls_r(dest_coords[0], dest_coords[1])

    def _reset_cells_visited(self):
        for cols in range(self.num_cols):
            for rows in range(self.num_rows):
                self.cells[cols][rows].visited = False




