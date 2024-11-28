from gui import *
import time
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
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = [] #Matrix of Cells      

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

        self._draw_cell()

        pass
    
    def _draw_cell(self):
        
        for column in self._cells:
            for cell in column:
                cell.draw()
                self._animate()



        
    
    def _animate(self):
        self._win.redraw()
        time.sleep(0.01)
    