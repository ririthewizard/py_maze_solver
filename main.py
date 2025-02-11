from graphics import *
from maze import *

def main():
    height = 600
    width = 800
    main_window = Window(width, height)
    maze = Maze(20, 20, 10, 10, 50, 50, main_window)
    #cell_one = Cell(main_window, Point(100, 100), Point(400, 400))
    #cell_one.__draw_cell()
    maze._create_cells()
  
    main_window.wait_for_close()

main()