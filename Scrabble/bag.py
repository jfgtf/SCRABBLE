from typing import NoReturn
from random import randint, shuffle


# Wymagane jest aby gracze korzystali z tej samej instancji klasy Bag()


class Bag:
    """
    It is the bag which is filled with all the letters which are available during the game
    """

    def __init__(self):
        self.letter_list = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'C', 'C', 'D', 'D',
                            'D', 'D', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'F', 'F', 'G', 'G',
                            'G',
                            'H', 'H', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'J', 'K', 'L', 'L', 'L', 'L', 'M',
                            'M',
                            'N', 'N', 'N', 'N', 'N', 'N', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'P', 'P', 'Q', 'R',
                            'R',
                            'R', 'R', 'R', 'R', 'S', 'S', 'S', 'S', 'T', 'T', 'T', 'T', 'T', 'T', 'U', 'U', 'U', 'U',
                            'V',
                            'V', 'W', 'W', 'X', 'Y', 'Y', 'Z']

        # self.letter_list = ['N', 'O', 'A', 'R', 'S', 'I', 'I', 'J', 'Z', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'J', 'K', 'L', 'L', 'L', 'L', 'M',
        #                     'M', 'N', 'N', 'O', 'O', 'O', 'O', 'R', 'S', 'S', 'T', 'T', 'T',]

        shuffle(self.letter_list)

        # Letters which has been removed from the bag
        self.popped_letters = []

    def get_size_of_bag(self):
        return len(self.letter_list)

    def generate_rack_for_player(self) -> list:
        # We are defining the player's rack which is going to be filled with letters
        rack_of_player = []

        while len(rack_of_player) != 7:
            letter = self.generate_letter_from_bag()
            rack_of_player.append(letter)

        # Player gets the rack filled with 7 letters
        return rack_of_player

    def update_of_main_bag(self, which_letter: str) -> NoReturn:
        """
        Update of the main bag of the game to be aware which letters are available for future pick.
        It is aux function which have usage in other functions of Bag class.

        PARAMETERS:
            which_letter: str
                Determinates which letter we want to update in our bag
        """

        # Which letter has been taken by the player
        self.letter_list.remove(which_letter)

    def generate_letter_from_bag(self) -> str:
        """
        Generating the letter from the main bag. We just return here letter as a letter not a key of our
        self.scrabble_letters_values
        """

        size_of_bag = len(self.letter_list)
        letter = self.letter_list[randint(0, size_of_bag - 1)]
        self.update_of_main_bag(letter)

        return letter

    def swap_letters(self, which_letter: str) -> str:
        size_of_bag = self.get_size_of_bag()
        letter = self.letter_list[randint(0, size_of_bag - 1)]
        self.update_of_main_bag(letter)
        self.letter_list.append(which_letter)

        return letter

    def add_letter_to_rack(self) -> str:
        """Adding the letter to the rack of player"""

        return letter

    def get_scrabble_letters_values(self):
        """
        Getting remaining letters from the main bag. It shows possibilities
        of what player might take on his rack
        """

        return self.scrabble_letters_values

    def get_popped_letters(self):
        """
        This method shows which letters are unavailable to pick from the bag
        """

        return self.popped_letters
