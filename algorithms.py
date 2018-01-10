__author__ = 'jdubois'


def countCellValueInList(cellValue, cellList):
    return sum( 1 for cell in cellList if cell.value == cellValue )

class Solver(object):

    @staticmethod
    def deduction_solve(grille):
        full_set = set([i for i in range(1,10)])
        nb_cells_changed = 1
        iteration = 0
        empty_cells_filled = set([])
        while nb_cells_changed > 0:
            print("ITERATION",iteration,": empty cells =",len(grille.empty_cells))
            nb_cells_changed = 0
            for c in grille.empty_cells:
                values_in_line = set(cell.value for cell in grille.lines[c.line])
                values_in_column = set(cell.value for cell in grille.columns[c.column])
                values_in_subgrid = set(c.subgrid.get_values())
                c.fill_cell_if_possible(values_in_line, values_in_column, values_in_subgrid)
                if c.isFilled():
                    empty_cells_filled.add(c)
                    nb_cells_changed += 1
            grille.empty_cells = grille.empty_cells.difference(empty_cells_filled)
            empty_cells_filled = set([])
            iteration += 1

    @staticmethod
    def try_to_fill_randomly(grille, first = False, recursion = 0, list_ = [], ordered_cells = []):
        # Trying to fill each empty cell
        for c in ordered_cells:
            #print("history",len(list_),":",str(list_))
            #print("Trying to fill grid from cell",c.line,c.column," which has possibilities:",c.possibilities)
            # Trying each possibility of chosen empty cell
            for p in c.possibilities:
                #print("Trying possibility",p,"for cell",c.line,c.column)
                #putting chosen value in chosen cell
                grille.fill_empty_cell_with_value(c,p)
                # If chosen value does not respect sudoku: stopping recusrion
                validGrid = Solver.test_grid_respect_sudoku_rules(grille,c,debug = False)
                if not validGrid:
                    #print("Sudoku rules not respected, stopping recursion")
                    pass
                else:
                    #if sudoku rules still respected after chosen possibility insertion: maybe grid is filled
                    if grille.isFilled():
                        #print("Grid is filled OK")
                        # if grid is filled then we got one possibility
                        return 0
                    else:
                        # if grid is not filled, then we carry on recursion on other empty cells
                        #if [c.line,c.column] in list_ : raise Exception("Trying one more time on already tried pair")
                        #list_.append([c.line,c.column])
                        cleared_ordered_cells = list(filter(lambda val: val != c, ordered_cells))

                        retSolverCode = Solver.try_to_fill_randomly(grille, recursion = recursion + 1, list_ = list_, ordered_cells = cleared_ordered_cells )
                        #Either recursion was unable to fill grid == -1
                        if retSolverCode == -1:
                            # if return code == -1 then we tried all possibilities below and got no solution
                            #print("No more possibility below",c.line,c.column,"for possibility",p)
                            #list_.remove([c.line,c.column])
                            pass
                        # or retCode != -1 => ==0 => gridfilled
                        else:
                            # We filled grid with recursion: then we have one possibility
                            return 0
                # if no return has been encountered, then we must empty the current cell
                grille.empty_cell(c)
            #print("No more possibilities for",c.line,c.column)
            # We have tried all possibilities, and so we signal it to the caller function
            return -1

    def test_grid_respect_sudoku_rules(grille, cell, debug = False):
        cellValue = cell.value

        lineNumber = cell.line
        line = grille.lines[lineNumber]
        cellValueCountLine = countCellValueInList(cellValue, line)
        if cellValueCountLine != 1: return False

        columnNumber = cell.column
        column = grille.columns[columnNumber]
        cellValueCountColumn = countCellValueInList(cellValue, column)
        if cellValueCountColumn != 1: return False

        subgrid = cell.subgrid.cases
        cellValueCountSubgrid = countCellValueInList(cellValue, subgrid)
        return cellValueCountSubgrid == 1
