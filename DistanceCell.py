"""Distance cell class."""
from Cell import Cell


class DistanceCell(Cell):

    def __init__(self, xcase, ycase, xtresor, ytresor):
        Cell.__init__(self, xcase, ycase, xtresor, ytresor)

    def visit(self):
        print("\n------------\n| Distance |\n------------\n")
        distance = abs(self._x-self._treasureX)+abs(self._y-self._treasureY)
        print(f"Le tresor se trouve a une distance d'environ {distance} cases.\n")
        self._isVisited=True
        return False
