__author__ = 'jdubois'

from case import Case
from subgrid import Subgrid

class CellList(object):

    def __init__(self, id):
        self.id = id
        self.cells = list()

    def addCell(self, cell):
        self.cells.append(cell)

    def getCell(self, idx):
        return self.cells[idx]

    def get_values(self):
        return [c.value for c in self.cells ]

class CellLine( CellList):

    def __init__(self, id, listOfCells):
        super().__init__(id)
        for c in listOfCells:
            self.addCell(c)

    def addCell(self, cell):
        super().addCell(cell)
        cell.setLine(self)

    def display(self):
        for nb_col, c in enumerate(self.cells):
            if c.value:
                print(' ' + str(c.value) + ' ' + '|', end='')
            else:
                print('   ' + '|', end='')

class CellColumn(CellList):

    def __init__(self, id, listOfCells):
        super().__init__(id)
        for c in listOfCells:
            self.addCell(c)

    def addCell(self, cell):
        super().addCell(cell)
        cell.setColumn(self)



class SudokuGrid (object):

    def __init__(self, file_to_open):
        # Creation of cells list in 1D
        self.cases = [Case() for i in range(81)]
        # Creation of 9 lists of references to cells corresponding to 9 lines
        # Creation of 9 lists of references to cells corresponding to 9 columns
        self.lines = []
        self.columns = []
        for l in range(9):
            cellLine = CellLine(l, self.cases[l*9:(l+1)*9])
            cellColumn = CellColumn(l, self.cases[l:81:9])
            self.columns.append(cellColumn)
            self.lines.append(cellLine)

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

        for c in self.empty_cells:
            c.updatePossibilities()

    def put_element(self, empty_cell, value):
        self.lines[empty_cell.cellLine.id].getCell(empty_cell.cellColumn.id).value = value

    def isFilled(self):
        return len(self.empty_cells) == 0

    def fill_empty_cell_with_value(self, cell, value):
        if cell in self.empty_cells:
            self.put_element(cell,value)
            self.removeEmptyCell(cell)
        else: raise Exception("Cannot put value in a non empty cell")

    def empty_cell(self, cell):
        if cell not in self.empty_cells:
            cell.reset_cell()
            self.empty_cells.add(cell)
        else: raise Exception("Cannot empty a cell that is already empty")

    def updatePossibilities(self):
        for c in self.empty_cells:
            c.updatePossibilities()

    def removeEmptyCell(self, cell):
        self.empty_cells.remove(cell)

    def removeEmptyCells(self, cellSet):
        self.empty_cells = self.empty_cells - cellSet