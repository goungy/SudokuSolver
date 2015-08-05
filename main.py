__author__ = 'jdubois'

from grid import SudokuGrid
from gui import Gui
from algorithms import Solver

file_to_open = "data/test_easy.txt"
file_to_open = "data/test_hard.txt"

grille = SudokuGrid(file_to_open)

g = Gui()

print("Displaying original grid")
g.display(grille)

Solver.deduction_solve(grille)

print("Displaying grid after first logical deductions")
g.display(grille)

#print("overall possibilities:",sum([len(cell.possibilities) for cell in grille.empty_cells],0),"for a total of",len(grille.empty_cells))

ordered_cells = sorted(grille.empty_cells, key = lambda cell: len(cell.possibilities))
if len(ordered_cells) > 0:
    print("Trying remaining possibilities on empty cells")
    Solver.try_to_fill_randomly(grille, ordered_cells = ordered_cells)

if grille.isFilled():
    print("Displaying final grid")
    g.display(grille)