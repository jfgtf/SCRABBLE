from bag import Bag
from typing import NoReturn

# ta sama klasa Baga musi być dla każdego Racka
# pomysł odziedziczenia klasy Bag przez BagOfGame

class Rack:
    """
    It is the rack which each player holds during the game.
    Letters are located on the rack and this rack indicates which letters
    might be used by player to create the word
    """
    bag = Bag()

    # def __init__(self):
    #     self.rack = Rack.bag.generate_rack_for_player()

    def get_rack(self):
        """This function returns the player's rack"""

        return self.rack

    def get_letter_from_bag(self) -> NoReturn:
        """
        This function is obliged to get the letter from the bag
        to the rack in case of missed round
        """

        # Generating the letter from the bag to the rack
        letter = Rack.bag.generate_letter_from_bag()

        # Updating common bag of all players
        Rack.bag.update_of_main_bag(letter)

        # Getting the value of letter
        value_of_letter = Rack.bag.scrabble_letters_values.get(letter)[1]

        # Initializing first occurence of the letter on our rack
        if not isinstance(self.rack.get(letter), list):
            up_player_rack = {letter: [1, value_of_letter]}
            self.rack.update(up_player_rack)

        # Adding letter which is already on our rack
        else:
            number_of_letter = self.rack.get(letter)[0]
            up_player_rack = {letter: [number_of_letter + 1, value_of_letter]}
            self.rack.update(up_player_rack)

    def remove_letter_from_rack(self, list_of_put_letters: list) -> NoReturn:
        """
        After putting the letter on the board we need to update
        our rack
        """
        #BEDZIEMY POTRZEBOWALI FUNKCJI, KTORA SPRAWDZA POPRAWNOŚĆ SLOWA POLOZONEGO NA TABLICY

        for index, letter in enumerate(list_of_put_letters):

            # Checking the number of letters on our rack
            number_of_letter = self.rack.get(letter)[0]

            # Removing completely the letter from our rack
            if number_of_letter == 1:
                self.rack.pop(letter)

            # Minus one letter from our rack
            else:
                value_of_letter = self.rack.get(letter)[1]

                # up ~ update
                up_player_rack = {letter: [number_of_letter - 1, value_of_letter]}
                self.rack.update(up_player_rack)

    @classmethod
    def reset_bag_for_racks(cls) -> NoReturn:
        """Should be used after every game to have fresh new bag"""

        Rack.bag = Bag()