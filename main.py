from graphics import *

def main():
    main_window = Window(800, 600)
    temp_cell = Cell(main_window, Point(100, 200), Point(300, 400))
    temp_cell.draw_cell()

    main_window.wait_for_close()

main()