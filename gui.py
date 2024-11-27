from tkinter import Tk, BOTH, Canvas
class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver v1")
        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=True)
        self.__isRunning = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
   
    def wait_for_close(self):
        self.__isRunning = True
        while self.__isRunning == True:
            self.redraw()
        
    def close(self):
        self.__isRunning = False
    
    def draw_line(self, Line, fill_color):
        Line.draw(self.__canvas, fill_color)
    

        
        
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.p1.x,
            self.p1.y,
            self.p2.x,
            self.p2.y,
            fill=fill_color,
            width = 2
        )

class Cell:
    def __init__(self, x1, y1, x2, y2, window_class):
        self._pointTL = Point(x1,y1)
        self._pointTR = Point(x1, y2)
        self._pointBL = Point(x2,y1)
        self._pointBR = Point(x2, y2)
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._win = window_class
        self.color = "black"
    
    def draw(self):
        if self.has_left_wall == True:
            left_wall = Line(self._pointTL, self._pointBL)
            self._win.draw_line(left_wall, self.color)
        if self.has_right_wall == True:
            right_wall = Line(self._pointTR, self._pointBR)
            self._win.draw_line(right_wall, self.color)
        if self.has_top_wall == True:
            top_wall = Line(self._pointTL, self._pointTR)
            self._win.draw_line(top_wall, self.color)
        if self.has_bottom_wall == True:
            bot_wall = Line(self._pointBL, self._pointBR)
            self._win.draw_line(bot_wall, self.color)
            

        


