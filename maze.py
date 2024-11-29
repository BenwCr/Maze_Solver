from gui import *
import time
import random
class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
        seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = [] #Matrix of Cells    

        if seed != None:
            random.seed(seed)  

        self._create_cells()

    def __repr__(self):
        return f"[{self._num_rows} x {self._num_cols}] {self._cells}"
    

    def _create_cell(self, x1, y1): #used in _create_cells
        return Cell(x1, y1, x1 + self._cell_size_x, y1 + self._cell_size_y,self._win)

    def _create_cells(self):
        row_num = 1
        x = self._x1
        y = self._y1
        while row_num <= self._num_rows:
            col_num = 1
            col_cell = []
            while col_num <= self._num_cols:
                col_cell.append(self._create_cell(x, y))
                x += self._cell_size_x
                col_num += 1
            self._cells.append(col_cell)
            x = self._x1
            y += self._cell_size_y
            row_num += 1
        
        self._break_entrance_and_exit()

        self._break_walls_r(0,0)

        self._reset_cells_visited()

        self._draw_cell()

        self._win.redraw()
        time.sleep(5)

        self.solve()

    def _break_entrance_and_exit(self):
        entrance = self._cells[0][0]
        exit = self._cells[-1][-1]
        entrance.has_left_wall = False
        exit.has_right_wall = False
        self._cells[0][0] = entrance
        self._cells[-1][-1] = exit
    
    

    def _break_walls_r(self, row, col): # (0, 0) top right corner (max, max) is bottom left corner
        self._cells[row][col].visited = True
        while True:
            valid_cells = []
            if self._is_valid_cell(row, col - 1) == True:
                valid_cells.append([row, col - 1,'l'])
            if self._is_valid_cell(row, col + 1) == True:
                valid_cells.append([row, col + 1, 'r'])
            if self._is_valid_cell(row - 1, col) == True:
                valid_cells.append([row - 1, col, 't'])
            if self._is_valid_cell(row + 1, col) == True:
                valid_cells.append([row+1, col, 'b'])
            if len(valid_cells) == 0:
                return
            next_cell = valid_cells[random.randrange(0, len(valid_cells))]
            if next_cell[2] == 'l':
                self._cells[row][col].has_left_wall = False
                self._cells[row][col - 1].has_right_wall = False
            elif next_cell[2] == 'r':
                self._cells[row][col].has_right_wall = False
                self._cells[row][col + 1].has_left_wall = False
            elif next_cell[2] == 'b':
                self._cells[row][col].has_bottom_wall = False
                self._cells[row + 1][col].has_top_wall = False
            elif next_cell[2] == 't':
                self._cells[row][col].has_top_wall = False
                self._cells[row - 1][col].has_bottom_wall = False
            else:
                raise Exception("valid cell error")
            #print(self._cells[row][col])
            #print(f"next: {next_cell}")
            self._break_walls_r(next_cell[0], next_cell[1])

        
    
    def _is_valid_cell(self, row, col): #cell in range of maze and NOT visited
        if row >= 0 and row < self._num_rows and col >= 0 and col < self._num_cols and self._cells[row][col].visited == False:
            return True
        return False



    def _reset_cells_visited(self):
        for r in range(self._num_rows):
            for c in range(self._num_cols):
                self._cells[r-1][c-1].visited = False



    def _draw_cell(self):
        
        for column in self._cells:
            for cell in column:
                cell.draw()
                #self._animate()

    
    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    
    def solve(self):
        if self.solve_r() == True:
            print ("horray!! Maze Solved")
        else:
            print ("awwww, Maze could not be solved")


    def solve_r(self, row=0,col=0):
        self._animate()
        self._cells[row][col].visited = True
        if row + 1 == self._num_rows and col + 1 == self._num_cols:
            return True
        if self._is_valid_cell(row + 1, col) == True and self._cells[row][col].has_bottom_wall == False:
            self._cells[row][col].draw_move(self._cells[row+1][col])
            if self.solve_r(row + 1, col) == True:
                return True
            self._cells[row][col].draw_move(self._cells[row+1][col],undo=True)

        if self._is_valid_cell(row - 1, col) == True and self._cells[row][col].has_top_wall == False:
            self._cells[row][col].draw_move(self._cells[row-1][col])
            if self.solve_r(row - 1, col) == True:
                return True
            self._cells[row][col].draw_move(self._cells[row-1][col],undo=True)
        
        if self._is_valid_cell(row, col + 1) == True and self._cells[row][col].has_right_wall == False:
            self._cells[row][col].draw_move(self._cells[row][col + 1])
            if self.solve_r(row, col + 1) == True:
                return True
            self._cells[row][col].draw_move(self._cells[row][col+1],undo=True)
            
        if self._is_valid_cell(row, col - 1) == True and self._cells[row][col].has_left_wall == False:
            self._cells[row][col].draw_move(self._cells[row][col - 1])
            if self.solve_r(row, col - 1) == True:
                return True
            self._cells[row][col].draw_move(self._cells[row][col -1],undo=True)
        return False
    
            
        
    