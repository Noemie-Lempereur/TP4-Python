"""Player class."""


class Player:
    """Define a player."""

    def __init__(self):
        """Initialize the player."""
        self.__name = 'Joueur'

    def askName(self):
        """Ask his name to the player."""
        self.__name = input('Entrez votre nom > ')
        if not self.__name.isalpha():
            print('Le nom est incorrect.')
            self.askName()

    def askXOrY(self, string, size):
        """Ask an x or y value according to the grid size."""
        value = input(string)
        if value.isdigit() and int(value) >= 1 and int(value) <= size:
            return int(value) - 1
        print('La valeur est incorrect.')
        return self.askXOrY(string, size)

    def getName(self):
        """Getter for name."""
        return self.__name
