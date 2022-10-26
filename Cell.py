"""Cell class."""

from abc import ABC, abstractmethod


class Cell(ABC):
    """Abstract class to define a cell."""

    def __init__(self, x, y, treasureX, treasureY):
        """Initialize the cell with position values."""
        self._x = x
        self._y = y
        self._treasureX = treasureX
        self._treasureY = treasureY
        self._isVisited = False

    def display(self):
        """Display a cell."""
        if self._isVisited:
            print('  ', end='')
        else:
            print('x ', end='')

    @abstractmethod
    def visit(self):
        """Abstract method to visit a cell."""
        raise NotImplementedError
        #pass


    def isVisited(self):
        """Getter for isVisited."""
        return self._isVisited

