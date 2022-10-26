"""Direction cell class."""

from Cell import Cell


class DirectionCell(Cell):

    def __init__(self, xcase, ycase, xtresor, ytresor):
        Cell.__init__(self, xcase, ycase, xtresor, ytresor)

    def visit(self):
        print("\n-------------\n| Direction |\n-------------\n")
        phrase="Le tresor se trouve"
        if self._treasureX < self._x:
            phrase+=" en haut"
        if self._treasureX > self._x:
            phrase+=" en bas"
        if self._treasureY < self._y:
            phrase+=" à gauche "
        if self._treasureY > self._y:
            phrase+=" à droite "
        print(phrase)
        print("\n")
        self._isVisited=True
        return False
