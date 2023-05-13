from typing import NoReturn
from random import randint, shuffle


# Wymagane jest aby gracze korzystali z tej samej instancji klasy Bag()


class Bag:
    """
    It is the bag which is filled with all the letters which are available during the game
    """

    def __init__(self):
        # letters_with_value = {str(letter): [int -> how many tiles of letter are in bag, int -> value of letter], ...}
        # self.scrabble_letters_values = {
        #     'A': 9, 'B': 12, 'C': 2, 'D': 4, 'E': 12, 'F': 2,
        #     'G': 3, 'H': 2, 'I': 9, 'J': 1, 'K': 1, 'L': 4,
        #     'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6,
        #     'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1,
        #     'Y': 2, 'Z': 1
        # }
        self.letter_list = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'C', 'C', 'D', 'D',
                            'D', 'D', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'F', 'F', 'G', 'G', 'G',
                            'H', 'H', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'J', 'K', 'L', 'L', 'L', 'L', 'M', 'M',
                            'N', 'N', 'N', 'N', 'N', 'N', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'P', 'P', 'Q', 'R', 'R',
                            'R', 'R', 'R', 'R', 'S', 'S', 'S', 'S', 'T', 'T', 'T', 'T', 'T', 'T', 'U', 'U', 'U', 'U', 'V',
                            'V', 'W', 'W', 'X', 'Y', 'Y', 'Z']

        shuffle(self.letter_list)        

        # Letters which has been removed from the bag
        self.popped_letters = []

    def get_size_of_bag(self):
        return len(self.letter_list)

    def generate_rack_for_player(self) -> list:

        # We are defining the player's rack which is going to be filled with letters
        rack_of_player = []

        while len(rack_of_player) != 7:

            # Gathering left letters from our main bag which are possible to take
            # Funkcje do tego tworzę generate letter from the bag
            '''available_letters = self.scrabble_letters_values.keys()

            # Getting the letter which exists in our main bag
            letter = list(available_letters)[random.randint(0, len(available_letters) - 1)]'''
            letter = self.generate_letter_from_bag()
            rack_of_player.append(letter)

            # """"(self.scrabble_letters_values.get(letter) is not None and""" było w if'ie poniżej

            # Check if the letter is actually initialized in player's rack. Line below indicates that letter hasn't been initialized
            """if not isinstance(rack_of_player.get(letter), list):
                # Initializing new letter in a player's bag
                up_player_rack = {letter: 1}
                rack_of_player.update(up_player_rack)

                # Update number of each letter in our main bag (because some of them are already taken by the players)
                self.update_of_main_bag(letter)

            # self.scrabble_letters_values.get(letter) is not None and | było w if'ie poniżej

            elif isinstance(rack_of_player.get(letter), list):
                # Add the letter to the player's bag which has been initialized before
                up_player_rack = {letter: self.scrabble_letters_values.get(letter)}
                rack_of_player.update(up_player_rack)

                # Update number of each letter in our main bag (because some of them are already taken by the players)
                self.update_of_main_bag(letter)

            else:
                continue"""

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
        #numbers_of_letter = self.scrabble_letters_values.get(which_letter)
        self.letter_list.remove(which_letter)

        """# Updating the number of letter which remains in the bag. It is decremented by 1
        if numbers_of_letter != 1:
            up_main_bag = {which_letter: self.scrabble_letters_values.get(which_letter) - 1}
            self.scrabble_letters_values.update(up_main_bag)

        # If number of this taken letter in the main bag is equal to 1 then letter is being removed from our main bag
        else:
            self.scrabble_letters_values.pop(which_letter)
            self.popped_letters.append(which_letter)"""

    def generate_letter_from_bag(self) -> str:
        """
        Generating the letter from the main bag. We just return here letter as a letter not a key of our
        self.scrabble_letters_values
        """

        # Gathering left letters from our main bag which are possible to take
        #available_letters = self.scrabble_letters_values.keys()

        # Getting the letter which exists in our main bag
        #letter = list(available_letters)[random.randint(0, len(available_letters) - 1)]
        size_of_bag = len(self.letter_list)
        letter = self.letter_list[randint(0, size_of_bag-1)]
        self.update_of_main_bag(letter)
        
        return letter

    def swap_letters(self, which_letter: str) -> str:

        size_of_bag = self.get_size_of_bag()
        letter = self.letter_list[randint(0, size_of_bag-1)]
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