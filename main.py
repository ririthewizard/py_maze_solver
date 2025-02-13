from graphics import *
from maze import *

def main():
    height = 600
    width = 800
    main_window = Window(width, height)
    maze = Maze(10, 10, 10, 10, 20, 20, main_window)

    main_window.wait_for_close()

main()
