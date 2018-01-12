__author__ = 'jdubois'

class Case(object):

    def __init__(self, value = 0):
        self.cellLine = None
        self.cellColumn = None
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

    def updatePossibilities(self):
        self.remove_possibilities(self.cellLine.get_values())
        self.remove_possibilities(self.cellColumn.get_values())
        self.remove_possibilities(set(self.subgrid.get_values()))

    def fill_cell_if_possible(self):

        if len(self.possibilities) == 1:
            print('found a value to put @ ', self.cellLine.id, self.cellColumn.id, self.possibilities)
            self.put_value(self.possibilities.pop())
            return True
        return False

    def put_value(self, value):
        if value not in range(1,10): raise Exception("Forbidden to put a value not in range 1-9")
        self.value = value

    def reset_cell(self):
        self.value = 0

    def setSubgrid(self, subgrid):
        self.subgrid = subgrid

    def setLine(self, cellLine):
        self.cellLine = cellLine

    def setColumn(self, cellColumn):
        self.cellColumn = cellColumn

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)