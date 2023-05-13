from bag import Bag
from typing import NoReturn

# ta sama klasa Baga musi być dla każdego Racka
# pomysł odziedziczenia klasy Bag przez BagOfGame
#zmiana nazwy klasy na Racks będzie bardziej adekwatna
class Rack:
    """
    It is the rack which each player holds during the game.
    Letters are located on the rack and this rack indicates which letters
    might be used by player to create the word
    """
    bag = Bag()


    @classmethod
    def reset_bag_for_racks(cls) -> NoReturn:
        """For future use"""

        Rack.bag = Bag()