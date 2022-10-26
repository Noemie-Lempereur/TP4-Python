"""Grid class."""
from DirectionCell import DirectionCell
from DistanceCell import DistanceCell
from TreasureCell import TreasureCell
from Player import Player
import random


class Grid:
    """Define a grid."""

    def __init__(self, size):
        """Initialize the grid."""
        self.__size = size
        self.__player = Player()
        self.__grid = [[0] * self.__size for x in range(0, self.__size)]

    def __initializeCells(self):
        xTreasure = random.randint(0, self.__size-1)
        yTreasure = random.randint(0, self.__size-1)
        print(yTreasure+1)
        print(xTreasure+1)
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                if yTreasure == j and xTreasure == i:
                    self.__grid[i][j] = TreasureCell(xTreasure, yTreasure)
                else:
                    valeur = random.randint(0, 4)
                    if valeur == 0:
                        self.__grid[i][j] = DistanceCell( i, j, xTreasure, yTreasure)
                    else:
                        self.__grid[i][j] = DirectionCell(i, j, xTreasure, yTreasure)

    def __display(self):
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                self.__grid[i][j].display()
            print("\r")

    def launch(self):
        """Launch the game."""
        # Initialize grid and player.
        self.__initializeCells()
        self.__player.askName()

        gameEnd = False
        while not gameEnd:
            # Display the grid.
            self.__display()

            # Ask the column and line.
            y = self.__player.askXOrY('Entrez la prochaine colonne a jouer > ',
                                      self.__size)
            x = self.__player.askXOrY('Entrez la prochaine ligne a jouer > ',
                                      self.__size)
            if self.__grid[x][y].isVisited():
                print('La case est déjà jouée.')
            else:
                gameEnd = self.__grid[x][y].visit()
        print('Bravo ' + self.__player.getName() + ' vous avez gagné.')
