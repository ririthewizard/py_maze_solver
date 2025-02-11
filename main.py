from graphics import *
from maze import *

def main():
    height = 600
    width = 800
    main_window = Window(width, height)
    maze = Maze(10, 10, 10, 10, 10, 10, main_window)

    maze._create_cells()
    maze._break_entrance_and_exit()

    main_window.wait_for_close()

main()