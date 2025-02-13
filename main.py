from graphics import *
from maze import *

def main():
    height = 600
    width = 800
    main_window = Window(width, height)
    maze = Maze(10, 10, 10, 10, 20, 20, main_window)

    maze._create_cells()
    maze._break_entrance_and_exit()
    maze._break_walls_r(0, 0)
    maze._reset_cells_visited()

    main_window.wait_for_close()

main()
