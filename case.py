__author__ = 'jdubois'

class Case(object):

    def __init__(self, line, column, value = 0):
        self.line = line
        self.column = column
        self.value = value
        self.subgrid = None
        self.possibilities = set([i for i in range(1,10)])
        if self.isEmpty(): self.possibilities = set([ i for i in range(1,10)])
        else: self.possibilities = self.value

    def isEmpty(self):
        return 0 == self.value

    def isFilled(self):
        return not self.isEmpty()

    def remove_possibilities(self, some_values):
        self.possibilities = self.possibilities.difference(some_values)

    def fill_cell_if_possible(self, values_in_line, values_in_column, values_in_subgrid):
        self.remove_possibilities(values_in_line)
        self.remove_possibilities(values_in_column)
        self.remove_possibilities(values_in_subgrid)

        if len(self.possibilities) == 1:
            print('found a value to put @ ', self.line, self.column, self.possibilities)
            self.put_value(self.possibilities.pop())

    def put_value(self, value):
        if value not in range(1,10): raise Exception("Forbidden to put a value not in range 1-9")
        self.value = value

    def reset_cell(self):
        self.value = 0

    def setSubgrid(self, subgrid):
        self.subgrid = subgrid

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)