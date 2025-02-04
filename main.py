from graphics import *

def main():
    main_window = Window(800, 600)
    l = Line(Point(400, 0), Point(400, 400))
    l2 = Line(Point(400, 300), Point(400, 300))
    main_window.draw_line(l, "black")
    main_window.draw_line(l2, "black")

    main_window.wait_for_close()

main()