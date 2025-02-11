from graphics import *
from maze import *

def main():
    height = 600
    width = 800
    main_window = Window(width, height)
    maze = Maze(10, 10, 20, 20, 20, 20, main_window)
    #cell_one = Cell(main_window, Point(100, 100), Point(400, 400))
    #cell_one.__draw_cell()
    maze._create_cells()
    maze._break_entrance_and_exit()
  
    main_window.wait_for_close()

main()