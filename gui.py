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
    
    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

        
        
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"({self.x}, {self.y})"

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
            width=2
        )
            
    def __repr__(self):
        return f"Point A ({self.p1.x},{self.p1.y}) | Point B ({self.p2.x},{self.p2.y})"

class Cell:
    def __init__(self, x1, y1, x2, y2, window_class):
        self._pointTL = Point(x1, y1)
        self._pointTR = Point(x2, y1)
        self._pointBL = Point(x1, y2)
        self._pointBR = Point(x2, y2)
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._win = window_class
        self.color = "black"
        self.visited = False
        self._pointCenter = Point((x1+x2)/2, (y1+y2)/2)

    def __repr__(self): 
        walls = ["L", "R", "T", "B"]   
        if self.has_left_wall == False:
            walls[0] = " "
        if self.has_right_wall == False:
            walls[1] = " "
        if self.has_top_wall == False:
            walls[2] = " "
        if self.has_bottom_wall == False:
            walls[3] = " "
            
        return f"TL: {self._pointTL}, TR: {self._pointTR}, BL: {self._pointBL}, BR: {self._pointBR}, Center: {self._pointCenter}, Walls: {walls}"
        return f"{self._pointTL}"
    
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
        
    def provide_center(self):
        return self._pointCenter
    
    def draw_move(self, to_cell, undo=False):
        line = Line(self._pointCenter, to_cell.provide_center())
        if undo == True:
            self._win.draw_line(line, "red")
        if undo == False:
            self._win.draw_line(line, "gray")



        


