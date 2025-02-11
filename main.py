from graphics import *
from maze import *

def main():
    main_window = Window(800, 600)
    maze = Maze(0, 0, 10, 10, 10, 10, main_window)
    cell_one = Cell(main_window, Point(100, 100), Point(400, 400))
    cell_one.__draw_cell()

    print(maze.cells)
    main_window.wait_for_close()

main()