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

    win.wait_for_close()

main()