__author__ = 'jdubois'

from case import Case
from subgrid import Subgrid

class SudokuGrid (object):

    def __init__(self, file_to_open):
        # Creation of cells list in 1D
        self.cases = [Case(int(i / 9), i % 9) for i in range(81)]
        # Creation of 9 lists of references to cells corresponding to 9 lines
        self.lines = []
        for l in range(9):
            self.lines.append(self.cases[l*9:(l+1)*9])
        # Creation of 9 lists of references to cells corresponding to 9 columns
        self.columns = []
        for c in range(9):
            self.columns.append(self.cases[c:81:9])
        # Creation of 9 lists corresponding referencing cells to 9 blocks of 3x3
        # Cells of Sudoku table
        self.subgrids = []
        for c in range(3):
            subgrid_line = []
            for l in range(3):
                subgrid_line.append(Subgrid(self.lines, l, c))
            self.subgrids.append(subgrid_line)
        self.empty_cells = set([])
        with open(file_to_open) as f:
            for nb_line,line in enumerate(f):
                for nb_col,nb in enumerate(line.strip()):
                    elt = int(nb)
                    self.cases[nb_line*9+nb_col].value = elt
                    if elt == 0: self.empty_cells.add(self.cases[nb_line*9+nb_col])

    def put_element(self, empty_cell, value):
        self.lines[empty_cell.line][empty_cell.column].value = value

    def isFilled(self):
        return len(self.empty_cells) == 0

    def fill_empty_cell_with_value(self, cell, value):
        if cell in self.empty_cells:
            self.put_element(cell,value)
            self.empty_cells.remove(cell)
        else: raise Exception("Cannot put value in a non empty cell")

    def empty_cell(self, cell):
        if cell not in self.empty_cells:
            cell.reset_cell()
            self.empty_cells.add(cell)
        else: raise Exception("Cannot empty a cell that is already empty")