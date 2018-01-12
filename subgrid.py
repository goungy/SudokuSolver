__author__ = 'jdubois'


class Subgrid(object):
    def __init__(self, lines, line, column):
        #print("Creating subgrid",line,column,"from lines",str(lines))
        self.cases = []
        self.line = line
        self.column = column
        start_line = line * 3
        start_col = column * 3
        for l in lines[start_line:start_line+3]:
            cases = [ l.getCell(idx) for idx in range(start_col,start_col+3) ]
            self.cases.extend(cases)
            for c in cases: c.setSubgrid(self)

    def get_values(self):
        return [c.value for c in self.cases]