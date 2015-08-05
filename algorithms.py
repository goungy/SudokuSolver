__author__ = 'jdubois'

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
                if not Solver.test_grid_respect_sudoku_rules(grille,debug = False):
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

                        if Solver.try_to_fill_randomly(grille, recursion = recursion + 1, list_ = list_, ordered_cells = cleared_ordered_cells ) == -1:
                            # if return code == -1 then we tried all possibilities below and got no solution
                            #print("No more possibility below",c.line,c.column,"for possibility",p)
                            #list_.remove([c.line,c.column])
                            pass
                        elif grille.isFilled():
                            # Maybe we filled grid with recursion: then we have one possibility
                            return 0
                # if no return has been encountered, then we must empty the current cell and
                grille.empty_cell(c)
            #print("No more possibilities for",c.line,c.column)
            # We have tried all possibilities, and so we signal it to the caller function
            return -1

    def test_grid_respect_sudoku_rules(grille, debug = False):
        for idx,l in enumerate(grille.lines):
            l_values = list([c.value for c in l])
            l_without_zeros = list(filter(lambda val: val != 0, l_values))
            if len(l_without_zeros) > len(set(l_without_zeros)): return False
            if debug:
                print("Line",idx)
                print(str(l_without_zeros))
                print(str(set(l_without_zeros)))
        for idx,l in enumerate(grille.columns):
            l_values = list([c.value for c in l])
            l_without_zeros = list(filter(lambda val: val != 0, l_values))
            if len(l_without_zeros) > len(set(l_without_zeros)): return False
            if debug:
                print("Column",idx)
                print(str(l_without_zeros))
                print(str(set(l_without_zeros)))
        for idxl,l_s in enumerate(grille.subgrids):
            for idxc,c_s in enumerate(l_s):
                l_values = list([c.value for c in c_s.cases])
                l_without_zeros = list(filter(lambda val: val != 0, l_values))
                if len(l_without_zeros) > len(set(l_without_zeros)): return False
                if debug:
                    print("Subgrid",idxl,idxc)
                    print(str(l_without_zeros))
                    print(str(set(l_without_zeros)))
        return True
        pass