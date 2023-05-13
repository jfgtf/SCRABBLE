from rack import Rack


class Player:
    """This class will hold information involved with information of user
    who has registered to play the game
    """
    # email, password do wyrzucenia
    def __init__(self, name: str, rack: list):
        self._name = name
        #self.rack jeszcze do ustalenia czy to atrybut gracza będzie...
        self.rack = rack
        self._score = 0
        # After 6-8 swaps the player ends his game
        self.missed = 0

    @property
    def name(self) -> str:
        return self._name

    @property
    def score(self) -> int:
        return self._score

    @name.setter
    def name(self, new_name: str):
        self._name = new_name

    @score.setter
    def score(self, points_add: int):
        self._score += points_add
