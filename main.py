from graphics import *

def main():
    main_window = Window(800, 600)

    temp_cell = Cell(main_window, Point(10, 10), Point(50, 50))
    temp_cell_two = Cell(main_window, Point(100, 10), Point(140, 50))
    temp_cell.draw_cell()
    temp_cell_two.draw_cell()
    
    temp_cell.draw_move(temp_cell_two, undo=True)

    main_window.wait_for_close()

main()