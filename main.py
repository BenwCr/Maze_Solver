from gui import *
def main():
    win = Window(800,600)

    P1 = Point(5, 200)
    P2 = Point(200, 5)
    P3 = Point(430, 290)
    P4 = Point(290,430)
    L1 = Line(P1, P4)
    L2 = Line(P3,P4)

    win.draw_line(L1, "black")
    win.draw_line(L2,"red")


    #C1 = Cell(100,100,200,200,win)
    #C1.draw()

    c = Cell(50, 50, 100, 100, win)
    c.has_left_wall = False
    c.draw()

    c = Cell(125, 125, 200, 200, win)
    c.has_right_wall = False
    c.draw()

    c = Cell(225, 225, 250, 250, win)
    c.has_bottom_wall = False
    c.draw()

    c = Cell(300, 300, 500, 500, win)
    c.has_top_wall = False
    c.draw()


    win.wait_for_close()

main()