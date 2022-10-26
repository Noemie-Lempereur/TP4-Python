"""Treasure cell class."""

from Cell import Cell


class TreasureCell(Cell):

    def __init__(self, xtresor, ytresor):
        Cell.__init__(self, xtresor, ytresor, xtresor, ytresor)

    def visit(self):
        return True
