from gui import *
from maze import *
def main():
    win = Window(800,600)

    maze = Maze(50,50,50,50,10,10,win)
    print(maze)




    win.wait_for_close()

main()