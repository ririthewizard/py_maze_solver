from graphics import *
from maze import *

def main():
    height = 600
    width = 800
    num_cols = 20
    num_rows = 20
    margin = 50
    cell_size_x = (width -2 * margin) / 20
    cell_size_y = (height -2 * margin) / 20


    main_window = Window(width, height)
    maze = Maze(margin, margin, num_cols, num_rows, num_cols, num_rows, main_window,) 
    maze.solve()

    main_window.wait_for_close()

main()
