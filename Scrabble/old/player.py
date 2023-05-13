from rack import Rack

# Będzie problem z zestawieniem nowego baga przy kolejnej grze jesli nie wylaczymy appki

class Player:
    """This class will hold information involved with information of user
    who has registered to play the game
    """

    # def __init__(self, name: str, email: str, password: str, rack: Rack):
    #     self.name = name
    #     self.email = email
    #     self.password = self.encrypt(password)
    #     # self.rack jeszcze do ustalenia czy to atrybut gracza będzie...
    #     self.rack = rack.rack
    #     self.score = 0
    #     # After 6-8 swaps the player ends his game
    #     swaps = 0

    def setName(self, new_name):
        self.name = new_name

    @property
    def name(self) -> str:
        return self._name

    @property
    def email(self) -> str:
        return self._email

    @property
    def password(self) -> str:
        return self._password

    @name.setter
    def name(self, new_name: str):
        self._name = new_name

    @email.setter
    def email(self, value: str):
        self._email = value

    @password.setter
    def password(self, new_password: str):
        self._password = self.encrypt(new_password)

    @property
    def score(self) -> int:
        return self._score

    @score.setter
    def score(self, points_add: int):
        self._score += points_add

    def encrypt(self, password_) -> str:
        password_ = bytes(password_, 'utf-8')
        return hashlib.sha256(password_).hexdigest()