from graphics import *
from maze import *

def main():
    height = 600
    width = 800
    main_window = Window(width, height)
    maze = Maze(10, 10, 10, 10, 10, 10, main_window)
    #cell_one = Cell(main_window, Point(100, 100), Point(400, 400))
    #cell_one.__draw_cell()
    maze._create_cells()
    maze._break_entrance_and_exit()
    print(maze.cells[0][0].walls["top_wall"])
    print(maze.cells[maze.num_rows - 1][maze.num_cols - 1].walls["bottom_wall"])

    main_window.wait_for_close()

main()