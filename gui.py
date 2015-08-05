__author__ = 'jdubois'

class Gui(object):

    def display_empty_line(self):
        print('-   |',end='')
        print("".join(['---+' for i in range(8)]),end='')
        print('---|')

    def display_strong_line(self):
        print('=   o',end='')
        print("".join(['===========#' for i in range(2)]),end='')
        print('===========o')

    def display_top_line(self):
        print('=   o',end='')
        print("".join(['============' for i in range(2)]),end='')
        print('===========o')

    def display(self, grid):
        lines = grid.lines
        print("    ",end='')
        print("".join(['| ' + str(i) + ' ' for i in range(9)]),end='')
        print('|')
        print()
        self.display_top_line()
        for nb_line,l in enumerate(lines):
            print(str(nb_line) + "   |",end='')
            for nb_col,c in enumerate(l):
                if c.value: print(' ' + str(c.value) + ' ' +'|',end='')
                else: print('   ' +'|',end='')
            print()
            if nb_line == 8: self.display_top_line()
            elif (nb_line + 1) % 3 == 0: self.display_strong_line()
            else: self.display_empty_line()

