from graphics import *
from maze import *

def main():
    main_window = Window(800, 600)
    maze = Maze(0, 0, 10, 10, 10, 10, main_window)

    print(maze.cells)
    main_window.wait_for_close()

main()