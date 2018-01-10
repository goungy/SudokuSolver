__author__ = 'jdubois'

from grid import SudokuGrid
from gui import Gui
from algorithms import Solver

import time

startTime = time.time()

file_to_open = "data/test_easy.txt"
file_to_open = "data/test_hard.txt"
file_to_open = "data/test1.txt"
file_to_open = "data/test_empty.txt"
file_to_open = "data/test_1233_easy.txt"
file_to_open = "data/test_512829_evil.txt"
file_to_open = "data/test_41187_devil.txt"

gridCreationStartTime = time.time()
grille = SudokuGrid(file_to_open)
gridCreationEndTime = time.time()
g = Gui()

print("Displaying original grid")
g.display(grille)

deductionStartTime = time.time()
Solver.deduction_solve(grille)
deductionEndTime = time.time()

print("Displaying grid after first logical deductions")
g.display(grille)

#print("overall possibilities:",sum([len(cell.possibilities) for cell in grille.empty_cells],0),"for a total of",len(grille.empty_cells))

ordered_cells = sorted(grille.empty_cells, key = lambda cell: len(cell.possibilities))
if len(ordered_cells) > 0:
    print("Trying remaining possibilities on empty cells")
    randomStartTime = time.time()
    Solver.try_to_fill_randomly(grille, ordered_cells = ordered_cells)
    randomFillEndTime = time.time()

if grille.isFilled():
    print("Displaying final grid")
    g.display(grille)

print("It took " + str(randomFillEndTime -  randomStartTime) + " to randomly fill the grid")