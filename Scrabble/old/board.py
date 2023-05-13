from __future__ import annotations
from itertools import chain
from word import Word
from collections import defaultdict
from player import Player
import copy
#wywalic set


# Gdzieś należy kopiować całą tablicę, w celu sprawdzenia store real and fake
# W playerze korzystamy z baga, więc nie musimy go importować
# Zawsze kopiujemy aktualny board

class Dictlist(dict):
    """This class allows us to update the key which has been already
    added to the dictionary
    """
    def __setitem__(self, key, value):
        try:
            self[key]
        except KeyError:
            super(Dictlist, self).__setitem__(key, [])
        self[key].append(value)


class Board:
    """This class implements all logic what happens on the board during the game"""

    # Standard ROW x COLUMNS scrabble's board. It is square.
    _size_board = 15


    _values_of_letters = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5,
                          'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4,
                          'W': 4, 'X': 8, 'Y': 4, 'Z': 10}

    def __init__(self):
        # None means empty field on the board
        self.actual_board = [['-' for i in range(Board._size_board)] for j in range(Board._size_board)]
        self.round = 1
        # Zmiana na z set na dict "SLOWO": [[X,Y],[X1,Y1]...[X4,Y4]]
        self.checked_words = {}
        # It storages the possibility of placing letters on the board \
        # 1 - Available place 2 - letter
        self.board_of_numbers = [[0 for i in range(15)] for j in range(15)]

        self._triple_word_score = [[0, 0], [7, 0], [14, 0], [0, 7], [14, 7], [0, 14], [7, 14], [14, 14]]

        self._double_word_score = [[1, 1], [2, 2], [3, 3], [4, 4], [1, 13], [2, 12], [3, 11], [4, 10], [13, 1],
                              [12, 2], [11, 3], [10, 4], [13, 13], [12, 12], [11, 11], [10, 10]]

        self._triple_letter_score =  [[1, 5], [1, 9], [5, 1], [5, 5], [5, 9], [5, 13], [9, 1], [9, 5],
                                    [9, 9], [9, 13], [13, 5], [13, 9]]

        self._double_letter_score = [
            [0, 3], [0, 11], [2, 6], [2, 8], [3, 0], [3, 7], [3, 14], [6, 2], [6, 6], [6, 8], [6, 12], [7, 3], [7, 11],
            [8, 2], [8, 6], [8, 8], [8, 12], [11, 0], [11, 7], [11, 14], [12, 6], [12, 8], [14, 3], [14, 11]]


    def get_copy_of_board(self):
        copy_board = copy.deepcopy(self.actual_board)
        return copy_board

    def game_turn(self):
        pass

    # wspolpracuje z place_letters
    # letters_with_coordinates from place_letters =
    def get_score(self, letters_with_coordinates: defaultdict(list), copy_board: list_of_lists) -> bool:
        # Metoda jak znajdzie _double/_triple_letter_score

        possible_moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        # It depends on if we will put a letter on TWS or DWS
        Multiplier = 1
        #possible_moves_ones = ((-1, 0), (1, 0), (0, 1), (0, -1))
        score = 0

        letters_put_in_tripleword = defaultdict(list)
        letters_put_in_doubleword = defaultdict(list)
        triple_words = []
        double_words = []
        alone_letters = []

        quantity_of_chars = {}
        # {letter: int, letter1: int1,...} explicit: {'K': 2, 'G': 2, ...}
        duplicate_letters = {}
        # Check if we put the same letters on the board
        for key, value in letters_with_coordinates.items():
            if len(value) > 1:
                duplicate_letters.update({key: len(value)})
                quantity_of_chars.update({key: len(value)})

            else:
                quantity_of_chars.update({key: len(value)})



        # Check if a letter is put on triple or double word score
        # e.g when we put more than one same type of letter like 2xA
        if duplicate_letters != {}:

            for duplicate_letter in duplicate_letters:

                # the number of loops is the number of particular letter {'K': 2} so loop will be repeated two times max
                for number_of_letter in range(duplicate_letters.get(duplicate_letter)):

                    #for coords_of_put_letter in letters_with_coordinates.get(duplicate_letter)[number_of_letter]... We gets here e.g [3,3]
                    coords_of_put_letter = letters_with_coordinates.get(duplicate_letter)[number_of_letter]

                    if coords_of_put_letter in self._triple_word_score:

                        # We are loking for coords of particular letter among words already checked and played to get to know \
                        # in which word the actually put letter is
                        for word, coords_of_word in self.checked_words.items():

                            # And here we are checking if the particular cords of put letter appears in certain word
                            # Przy .items() nasze .values() oplata dodatkowa lista
                            # self.checked_words = {WORD: [[[2,3],[4,5]]],...} len(self.checked_words.get('WORD')) == 1; len(self.checked_words.get('WORD')[0]) == 2;
                            # nwm czy tu coords_of_word[0] czy coords_fo_word po prostu
                            # Tutaj iterujemy współrzędne słowa: [1,1], [2,1]...
                            for coords_of_word_letter in coords_of_word:

                                # Dzisiaj tu pisałem//nieaktualne bo to juz nie dzisiaj:)
                                if coords_of_put_letter == coords_of_word_letter:
                                    # Probujemy usunąć inne litery położone na tablice w tym słowie. W celu nie duplikowania punktów.
                                    # coords_of_other_word_letter - inne liter dolozone w tej rundzie pomijająć literę, która się znajduje na TWS
                                    for coords_of_other_word_letter in coords_of_word:
                                        # for letter, coords_already_put in letters_with_coordinates.items(): looks like that:
                                        #A[[6, 7], [6, 8], [6, 9]]
                                        #B[[6, 3],[6,4]]
                                        #G[[10, 11],[11,11]]
                                        for letter, coords_already_put in letters_with_coordinates.items():
                                            # coords_of_put_letter is the tile on the cell TWS
                                            # Because this kind of letter is going to be handled later in this block of code
                                            if coords_of_put_letter == coords_of_other_word_letter:
                                                continue

                                            # ten blok poniżej służy usunięciu liter, które zostały już zagrane \
                                            # gdzie inna litera tego slowa znajduje sie na TWS \
                                            # jest to potzebne, aby nie duplikować potem liter przy obliczaniu punktów
                                            # Nie chodzi tu nam o litere na TWS, a pozostałe
                                            if coords_of_other_word_letter in coords_already_put:
                                                if len(letters_with_coordinates.get(letter)) == 1:
                                                    letters_with_coordinates.pop(letter)

                                                else:
                                                    # copy paste from the code which appears lower
                                                    # aktualizacja położonych kafelków na plansze
                                                    # np. kladziemy OOP , gdzie P znajduje się na TWS \
                                                    # a OO za L, a przed P \
                                                    # i musimy zaktualizować jedną z liter O \
                                                    # Potem w poętli następną\
                                                    # Aczkolwiek cały blok kodu od if duplicate_letters != \
                                                    # Opowiada ze szczególny przypadek
                                                    numbers_of_this_letter = len(letters_with_coordinates.get(letter))
                                                    letter_put_in_word_coords = letters_with_coordinates.get(letter)
                                                    left_coords = []
                                                    for i in range(numbers_of_this_letter):
                                                        # coords_of_put_letter will be handled later in this bloc of code
                                                        if letter_put_in_word_coords[i] == coords_of_put_letter:
                                                            continue
                                                        else:
                                                            left_coords.append(letter_put_in_word_coords[i])

                                                    # To może być niepotrzebne, a nawet błędem albo głupoty piszę (w sensie te zdanie)
                                                    letters_with_coordinates.update({duplicate_letter: left_coords})




                                    # TUTAJ UZUPEŁNIAMY
                                    # chyba jest git już powyżej...

                                    if word not in triple_words:
                                         triple_words.append(word)
                                         # linijka pod spodem do wyrzucenia najprawdopodobniej
                                         # Bo bedziemy splitować całe słowo, a co za tym idzie obliczać na podstawie słowa punkty, a nie położonych liter
                                         letters_put_in_tripleword[duplicate_letter].append(coords_of_put_letter)
                                         self._triple_word_score.remove(coords_of_put_letter)

                                         if len(letters_with_coordinates.get(duplicate_letter)) == 1:
                                            letters_with_coordinates.pop(duplicate_letter)

                                         else:
                                             coords_of_this_letter = letters_with_coordinates.get(duplicate_letter)[number_of_letter]
                                             # Kwestia aktualizacji kiedy bysmy mieli np. wiecej duplikaty cos tam elo ide spac
                                             # aktualizacja
                                             numbers_of_this_letter = len(letters_with_coordinates.get(duplicate_letter))
                                             left_coords = []
                                             for i in range(numbers_of_this_letter):
                                                 if coords_of_this_letter == coords_of_put_letter:
                                                     continue
                                                 else:
                                                     left_coords.append(letters_with_coordinates.get(duplicate_letter)[i])

                                             letters_with_coordinates.update({duplicate_letter: left_coords})


                                    else:

                                        self._triple_word_score.remove(coords_of_put_letter)

                                else:
                                    continue



                    # podobna sztuka co powyżej
                    elif coords_of_put_letter in self._double_word_score:

                        # self.checked_words = {WORD: [[[2,3],[4,5]]],...} len(self.checked_words.get('WORD')) == 1; len(self.checked_words.get('WORD')[0]) == 2;
                        for word, coords_of_word in self.checked_words.items():
                            # było for coords_of_letter in coords_of_word[0]
                            for coords_of_letter in coords_of_word:

                                # Copy paste z powyżej gdzie trafilibyśmy na TWS a nie na DWS
                                if coords_of_letter == coords_of_word:

                                    # Probujemy usunąć inne litery położone na tablice w tym słowie. W celu nie duplikowania punktów.
                                    # coords_of_other_word_letter - inne liter dolozone w tej rundzie pomijająć literę, która się znajduje na TWS
                                    for coords_of_other_word_letter in coords_of_word:
                                        # for letter, coords_already_put in letters_with_coordinates.items(): looks like that:
                                        # A[[6, 7], [6, 8], [6, 9]]
                                        # B[[6, 3],[6,4]]
                                        # G[[10, 11],[11,11]]
                                        for letter, coords_already_put in letters_with_coordinates.items():
                                            # coords_of_put_letter is the tile on the cell TWS
                                            # Because this kind of letter is going to be handled later in this block of code
                                            if coords_of_put_letter == coords_of_other_word_letter:
                                                continue

                                            # ten blok poniżej służy usunięciu liter, które zostały już zagrane \
                                            # gdzie inna litera tego slowa znajduje sie na TWS \
                                            # jest to potzebne, aby nie duplikować potem liter przy obliczaniu punktów
                                            # Nie chodzi tu nam o litere na TWS, a pozostałe
                                            if coords_of_other_word_letter in coords_already_put:
                                                if len(letters_with_coordinates.get(letter)) == 1:
                                                    letters_with_coordinates.pop(letter)

                                                else:
                                                    # copy paste from the code which appears lower
                                                    # aktualizacja położonych kafelków na plansze
                                                    # np. kladziemy OOP , gdzie P znajduje się na TWS \
                                                    # a OO za L, a przed P \
                                                    # i musimy zaktualizować jedną z liter O \
                                                    # Potem w poętli następną\
                                                    # Aczkolwiek cały blok kodu od if duplicate_letters != \
                                                    # Opowiada ze szczególny przypadek
                                                    numbers_of_this_letter = len(letters_with_coordinates.get(letter))
                                                    letter_put_in_word_coords = letters_with_coordinates.get(letter)
                                                    left_coords = []
                                                    for i in range(numbers_of_this_letter):
                                                        # coords_of_put_letter will be handled later in this bloc of code
                                                        if letter_put_in_word_coords[i] == coords_of_put_letter:
                                                            continue
                                                        else:
                                                            left_coords.append(letter_put_in_word_coords[i])

                                                    letters_with_coordinates.update({duplicate_letter: left_coords})





                                    if word not in double_words:
                                        double_words.append(word)
                                        # Do wywalenia i guess linijka poniżej
                                        letters_put_in_doubleword[put_letter].append(coords_of_put_letter)
                                        self._triple_word_score.remove(coords_of_put_letter)

                                        if len(letters_with_coordinates.get(duplicate_letter)) == 1:
                                            letters_with_coordinates.pop(put_letter)

                                        else:
                                            coords_of_this_letter = letters_with_coordinates.get(put_letter)[number_of_letter]
                                            # Kwestia aktualizacji kiedy bysmy mieli np. wiecej duplikaty cos tam elo ide spac
                                            # aktualizacja
                                            numbers_of_this_letter = len(letters_with_coordinates.get(duplicate_letter))
                                            left_coords = []
                                            for i in range(numbers_of_this_letter):
                                                if coords_of_this_letter == coords_of_put_letter:
                                                    continue
                                                else:
                                                    left_coords.append(
                                                        letters_with_coordinates.get(duplicate_letter)[i])

                                            letters_with_coordinates.update({duplicate_letter: left_coords})


                                    else:

                                        self._double_word_score.remove(coords_of_put_letter)
                                        # Skopiowałem i wkleiłem tera kwestia wyhandlować litery, które idą na puste pola i elo




        # Jeszcze raz to samo co na górze od if duplicate_letters != {}
        # Jeżeli byśmy nie mieli zduplikowanych liter, co zaoszczędziłoby nam zasoby elo
        # ----

        # To tutaj jest do wywalenia poniżej, bo inną myślą się kierujemy A NA PEWNO DO ZMIENIENIA
        # nie mamy duplikatów
        else:
            # Nasza struktura tutaj to: 'K': [[3,4]]
            for put_letter, coords_of_put_letter in letters_with_coordinates.items():

                # We access here nested list, it means coords: [3,4] e.g.
                coords_of_put_letter = coords_of_put_letter[0]

                if coords_of_put_letter in self._triple_word_score:

                    # self.checked_words = {WORD: [[2,3],[2,4],[2,5],[2,6]],...} len(self.checked_words.get('WORD')) == 4; len(self.checked_words.get('WORD')[0]) == 2;
                    for word, coords_of_word in self.checked_words.items():
                        # bylo: for coords_of_letter in coords_of_word[0]:
                        for coords_of_letter in coords_of_word:

                            # coords_of_put_letter to TWS
                            if coords_of_letter == coords_of_put_letter:
                                # tu gdzieś musi być jeszcze indeksowanie po key and value letters_with_coordinates by usuwać godzina 13:28
                                for coords_of_other_word_letter in coords_of_word:

                                    if coords_of_put_letter == coords_of_other_word_letter:
                                        # Letter on TWS will be handled later albo tutaj możemy...
                                        continue

                                    else:
                                        # Jeśli by było indekoswanie po key and value letters_with...(to co wyzej zasugerowalem)letters_with_coordinates.pop()
                                        # we get the letter by the line of code below:
                                        # możemy użyć tryów i except albo iterować po key and values letters_with_coordinates by usuwać...
                                        try:
                                            # get the KEY by VALUE
                                            letter_to_pop = list(letters_with_coordinates.keys())[list(letters_with_coordinates.values()).index([coords_of_other_word_letter])]
                                            # We can pop them or create new list for letters which are in DWS or TWS
                                            letters_with_coordinates.pop(letter_to_pop)
                                        except Exception as e:
                                            print("{}, this letter was put on the board not in your round".format(e))



                                if word not in triple_words:

                                    # if word not in triple_words musi tu być
                                    triple_words.append(word)
                                    # do wywalenia to poniżej, w sensie niepotrzebne to || A jednak może potrzebne do znajdywania pojedynczych liter
                                    letters_put_in_tripleword[put_letter].append(coords_of_put_letter)
                                    # NO TO JEST DO ROZWAŻENIA: LINIJKA PONIŻEJ: Dodajemy litery, które są użyte do TWS lub DWS lub usuwamy je kompletnie...
                                    letters_with_coordinates.pop(put_letter)
                                    self._triple_word_score.remove(coords_of_put_letter)


                elif coords_of_put_letter in self._double_word_score:

                    for word, coords_of_word in self.checked_words.items():

                        for coords_of_letter in coords_of_word:

                            # coords_of_put_letter to DWS
                            if coords_of_letter == coords_of_put_letter:
                                # tu gdzieś musi być jeszcze indeksowanie po key and value letters_with_coordinates by usuwać godzina 13:28
                                for coords_of_other_word_letter in coords_of_word:

                                    if coords_of_put_letter == coords_of_other_word_letter:
                                        # Letter on TWS will be handled later
                                        continue

                                    else:
                                        # Jeśli by było indekoswanie po key and value letters_with...(to co wyzej zasugerowalem)letters_with_coordinates.pop()
                                        # we get the letter by the line of code below:
                                        # możemy użyć tryów i except albo iterować po key and values letters_with_coordinates by usuwać...
                                        try:
                                            # Możemy skorzystać z "\"
                                            letter_to_pop = list(letters_with_coordinates.keys())[list(letters_with_coordinates.values()).index([coords_of_other_word_letter])]
                                            letters_with_coordinates.pop(letter_to_pop)
                                        except Exception as e:
                                            print("{}, this letter was put on the board not in your round".format(e))

                                # Teoretycznie zawsze będzie not in, ale tak pokręcona logika jest, \
                                # że po prostu upewniam się tu, że word not in double words...
                                # Zauważ, że to po loopie jest...
                                if word not in double_words:

                                    # if word not in triple_words musi tu być
                                    double_words.add(word)
                                    # do wywalenia to poniżej, w sensie niepotrzebne to
                                    letters_put_in_doubleword[put_letter].append(coords_of_put_letter)
                                    # CHYBA TRZEBA USUNĄĆ
                                    # Tego aktu nie dokonaliśmy chyba wyżej
                                    # Robimy tak no bo tutaj robimy triple'a/double'a słowa, a nie sumujemy pojedyczno położonyc liter \
                                    # za położenie OOP do L, liczymy punkty za LOOP, a L przecież nie położyliśmy, czaisz?
                                    letters_with_coordinates.pop(put_letter)
                                    try:
                                        self._double_word_score.remove(coords_of_put_letter)
                                    except Exception as e:
                                        print("Has been already removed")


        # TUTAJ OSOBNO JUŻ PO SPRAWDZENIU CZY MAMY TWS CZY DWS \
        # DODAJEMY POJEDYNCZE KAFELKI PONIŻEJ
        # NALEŻY JESZCZE PRZEJRZEĆ TE IF'y powyżej BO MOŻE ZDARZYĆ SIĘ SYTUACJA, ŻE \
        # BEDZIEMY MIELI DOUBLE LETTER + TWS np.
        # TERA TWORZĘ FUNKCJE DLA LITER, GDZIE NIE MAMY DUPLIKATÓW
        if duplicate_letters != {} and letters_with_coordinates != {}:

            #quantity of duplicate_letters = aux
            aux = len(duplicate_letters)
            auxv2 = list(duplicate_letters)
            #for duplicate_letter in duplicate_letters:
            for index in range(aux):
                duplicate_letter = auxv2[index]
                copies_of_letter = len(letters_with_coordinates.get(duplicate_letter))

                for number_of_letter in range(copies_of_letter):

                    letter_coords = letters_with_coordinates.get(duplicate_letter)[0]

                    if letter_coords in self._double_letter_score:

                        # 2 * value of letter which was put
                        score += 2 * self._values_of_letters.get(duplicate_letter)
                        self._double_letter_score.remove(letter_coords)
                        letters_with_coordinates.get(duplicate_letter).remove(letter_coords)

                    elif letter_coords in self._triple_letter_score:

                        # 3 * value of letter which was put
                        score += 3 * self._values_of_letters.get(duplicate_letter)
                        self._triple_letter_score.remove(letter_coords)
                        letters_with_coordinates.get(duplicate_letter).remove(letter_coords)

                    else:

                        score += self._values_of_letters.get(duplicate_letter)
                        letters_with_coordinates.get(duplicate_letter).remove(letter_coords)
                        duplicate_letters.update({duplicate_letter: duplicate_letters.get(duplicate_letter) - 1})
                        if duplicate_letters.get(duplicate_letter) == 0:
                            duplicate_letters.pop(duplicate_letter)
                            letters_with_coordinates.pop(duplicate_letter)



        if duplicate_letters == {} and letters_with_coordinates != {}:

            for put_letter in list(letters_with_coordinates):

                # We access here nested list, it means coords: [3,4] e.g.
                coords_of_put_letter = letters_with_coordinates.get(put_letter)[0]

                if coords_of_put_letter in self._double_letter_score:

                    score += 2 * self._values_of_letters.get(put_letter)
                    self._double_letter_score.remove(coords_of_put_letter)
                    letters_with_coordinates.pop(put_letter)

                elif coords_of_put_letter in self._triple_letter_score:

                    score += 3 * self._values_of_letters.get(put_letter)
                    self._triple_letter_score.remove(coords_of_put_letter)
                    letters_with_coordinates.pop(put_letter)

                else:
                    score += self._values_of_letters.get(put_letter)
                    letters_with_coordinates.pop(put_letter)



        # Here we are counting points from double_words and triple_words
        for word in range(len(triple_words)):
            letters_of_word = list(chain(triple_words[word]))
            for letter in letters_of_word:
                score += 3 * _values_of_letters.get(letter)

        for word in range(len(double_words)):
            letters_of_word = list(chain(triple_words[word]))
            for letter in letters_of_word:
                score += 2 * _values_of_letters.get(letter)

        return score


        # te wszystkie POP'y i ten warunek letters_with_coordinates != {} do ponownego rozpatrzenia...
        # pętle pętle i jeszcze raz pętle

    def place_letters(self, letters_put_by_player: list, coordinates: list_of_lists, copy_board: list_of_lists) -> defaultdict(list):
        # Te wszystkie copy_board to chyba jako parametr bedziemy przenosić
        # Ten copy_board to jednak do funkcji będzie przenoszony i tworzony jako jakiś global
        #copy_board = Board.get_copy_of_board()
        letter_coordinates = defaultdict(list)
        for index, letter in enumerate(letters_put_by_player):
            # index - Which in order coords of which letter, [0] - row , [1] - column \
            # and here we are initializing letters for our copy board
            copy_board[coordinates[index][0]][coordinates[index][1]] = letter
            letter_coordinates[letter].append(coordinates[index])

        return letter_coordinates

    def first_move(self, first_letters: list_of_lists, copy_board: list_of_lists, loaded_dictionary: dict) -> bool:
        #copy_board = Board.get_copy_of_board()

        if not [7,7] in first_letters:
            return False

        columns = list(zip(*copy_board))
        column_8th = columns[7]

        row_8th = copy_board[7]

        aux = False
        first_word = ""
        # False means we have not got, True means we have got our potential word on board \
        # with correct placement if we consider rules of first move in scrabble
        we_have_potential_word = False
        #Check 8th row
        for index, cell in enumerate(row_8th):
            # We enter this loop only once
            if cell != "-" and aux is False:
                # Coords of potential first word put on board
                potential_first_word = index
                first_word += row_8th[potential_first_word]
                while potential_first_word < 14:
                    # We have checked before if [7,7] is taken... So probably first word is put vertiacally \
                    # but still we have to check if there is no other tiles in 8th row
                    if row_8th[potential_first_word + 1] == "-" and potential_first_word + 1 < 7:
                        # Letter is not connected with [7,7]
                        return False

                    # We add another letter to the letter which has been found before and they are \
                    # continuous with each other on the 8th row
                    elif row_8th[potential_first_word + 1] != "-" and potential_first_word != "-":
                        first_word += row_8th[potential_first_word + 1]
                        potential_first_word += 1

                    elif row_8th[potential_first_word + 1] == "-" and potential_first_word + 1 > 7 \
                        and len(first_word) >= 2 and we_have_potential_word is False:
                        # But still we have to check the rest of row...
                        we_have_potential_word = True
                        #first_word += row_8th[potential_first_word + 1]
                        potential_first_word += 1
                        # So in next loops we are going to check if there are redundant tiles...

                    #elif copy_board[7][potential_first_word + 1] != "-" and potential_first_word + 1 > 7 \
                        #and we_have_potential_word is True:
                        # We have got the potential word and we have found tile after the word
                        #return False

                    elif row_8th[potential_first_word + 1] != "-" and we_have_potential_word is True:
                        return False

                    else:
                        potential_first_word += 1
                        if potential_first_word == 14:
                            aux = True
            
            elif cell != "-" and aux is True:
                break


                    #elif copy_board[7][potential_first_word + 1] != "-" and we_have_potential_word is True:

                    # to powinno być na końcu imo
                    #elif copy_board[7][potential_first_word + 1] != "-" and we_have_potential_word is True:
                    #first_word += copy_board[7][potential_first_word + 1]
                    #potential_first_word += 1
        aux = False
        if we_have_potential_word == False:
            for index, cell in enumerate(column_8th):
                if cell != "-" and aux is False:
                    # Coords of potential first word put on board
                    potential_first_word = index
                    first_word += column_8th[potential_first_word]
                    while potential_first_word < 14:
                        # We have checked before if [7,7] is taken... So probably first word is put vertiacally \
                        # but still we have to check if there is no other tiles in 8th row
                        if column_8th[potential_first_word + 1] == "-" and potential_first_word + 1 < 7:
                            # Letter is not connected with [7,7]
                            return False

                        # We add another letter to the letter which has been found before and they are \
                        # continuous with each other on the 8th row
                        elif column_8th[potential_first_word + 1] != "-" and potential_first_word != "-":
                            first_word += column_8th[potential_first_word + 1]
                            potential_first_word += 1

                        elif column_8th[potential_first_word + 1] == "-" and potential_first_word + 1 > 7 \
                                and len(first_word) >= 2 and we_have_potential_word is False:
                            # But still we have to check the rest of row...
                            we_have_potential_word = True
                            #first_word += column_8th[potential_first_word + 1]
                            potential_first_word += 1
                            # So in next loops we are going to check if there are redundant tiles...

                        # elif copy_board[7][potential_first_word + 1] != "-" and potential_first_word + 1 > 7 \
                        # and we_have_potential_word is True:
                        # We have got the potential word and we have found tile after the word
                        # return False

                        elif column_8th[potential_first_word + 1] != "-" and we_have_potential_word is True:
                            return False

                        else:
                            potential_first_word += 1
                            if potential_first_word == 14:
                                aux is True

                elif cell != "-" and aux is True:
                    break
        else:
            for index, cell in enumerate(column_8th):
                if cell != "-" and index != 7 :
                    # inappropriately put letter on board
                    return False


        # Check if we have got somewehre else a letter in spite of 8th row and 8th column
        for index_row in range(len(copy_board)):
            if index_row == 7:
                continue
            else:
                for index_column, cell in enumerate(copy_board[index_row]):
                    if index_column == 7:
                        continue
                    else:
                        if cell != "-":
                            # Because we can only put one word during the first move of first round...
                            return False




        # Now we are checking correctness of the word
        correctness_of_word = Word.check_validity_of_word(first_word, loaded_dictionary)

        if correctness_of_word is True:
            return True

        else:
            return False









    def create_sum_board_4_connection(self):
        """
        2 - letter, forbidden for swap
        1 - for future placement of letter
        0 - forbidden cell to place letter
        """
        possible_moves_ones = ((-1, 0), (1, 0), (0, 1), (0, -1))

        # Setting ones
        for i in range(len(self.actual_board)):
            for j in range(len(self.actual_board)):

                if self.actual_board[i][j] != "-":

                    # Setting ones around letter
                    for cell in possible_moves_ones:

                        try:

                            self.board_of_numbers[i + cell[0]][j + cell[1]] = 1

                        except Exception as e:
                            print('Out of bound but dont worry this error has been handled :-) And we are still in:-)')
                            continue

        # Setting 2 in place of letter
        for i in range(len(self.actual_board)):
            for j in range(len(self.actual_board)):

                if self.actual_board[i][j] != "-":
                    self.board_of_numbers[i][j] = 2

    # First in the use must be setting ones and twos
    def check_validity_placement_rows(self, copy_board: list_of_lists) -> bool:

        # copy_board - for rows
        #copy_board = Board.get_copy_of_board()
        # na copy_boardzie stawiamy litery, przed sprawdzeniem
        # copy_board_columns = list(zip(*copy_board))

        # [ROW, COLUMN]
        place_of_one = []

        place_of_two = []

        # for i in range(self.board_of_numbers):
        #   for j in range(self.board_of_numbers):
        for i in range(len(self.actual_board)):
            for j in range(len(self.actual_board)):

                if self.board_of_numbers[i][j] == 1:
                    place_of_one.append([i, j])

                elif self.board_of_numbers[i][j] == 2:
                    place_of_two.append([i, j])

                else:
                    continue

        new_words = []
        buffer_word = ""
        row_col_buff = []
        # checking rows
        # Nie wiem czy te i, j(aktualnie usunięte) dodawane do row_col_buff musi być szczerze...
        for i in range(len(copy_board)):
            for j in range(len(copy_board)):

                if j != 14:

                    if copy_board[i][j] != "-" and len(buffer_word) == 0:
                        buffer_word += copy_board[i][j]
                        row_col_buff.append([self.board_of_numbers[i][j]])

                    elif copy_board[i][j] != "-" and len(buffer_word) != 0:
                        buffer_word += copy_board[i][j]
                        row_col_buff.append([self.board_of_numbers[i][j]])

                    elif copy_board[i][j] == "-" and len(buffer_word) == 1:
                        buffer_word = ""
                        row_col_buff = []

                    elif copy_board[i][j] == "-" and len(buffer_word) > 1:
                        new_words.append([buffer_word, row_col_buff])
                        buffer_word = ""
                        row_col_buff = []

                    else:
                        continue

                else:

                    if copy_board[i][j] == "-" and len(buffer_word) <= 1:
                        buffer_word = ""
                        row_col_buff = []

                    elif copy_board[i][j] != "-" and len(buffer_word) >= 1:
                        buffer_word += copy_board[i][j]
                        row_col_buff.append([self.board_of_numbers[i][j]])
                        new_words.append([buffer_word, row_col_buff])
                        buffer_word = ""
                        row_col_buff = []

                    elif copy_board[i][j] == "-" and len(buffer_word) > 1:
                        new_words.append([buffer_word, row_col_buff])
                        buffer_word = ""
                        row_col_buff = []

                    else:
                        buffer_word = ""
                        row_col_buff = []
                        # End of inside loop

        # To check if actually put letters are in correct place
        checking_word = []
        for word in new_words:
            if not checking_word:
                pass

            else:

                if 1 in checking_word and 2 not in checking_word:
                    checking_word = []

                else:
                    print("Letters put on the board are not in the correct place on the board")
                    # Pomyśleć nad loggerami
                    return False
            # Jak usuniemy i, j z row_col to też musimy zmienić tu indeksy | Juz pomyslelismy nad tym i weszlo w zycie
            # word[1] looks like [[1],[0],[0],[1]]
            for j in word[1]:
                checking_word.append(j[0])

        return True

    # This function is the copy of function above
    def check_validity_placement_columns(self, copy_board: list_of_lists) -> bool:

        copy_board = list(zip(*copy_board))

        # na copy_boardzie stawiamy litery, przed sprawdzeniem
        # copy_board_columns = list(zip(*copy_board))

        # [ROW, COLUMN]
        place_of_one = []

        place_of_two = []

        # for i in range(self.board_of_numbers):
        #   for j in range(self.board_of_numbers):
        for i in range(len(self.actual_board)):
            for j in range(len(self.actual_board)):

                if self.board_of_numbers[i][j] == 1:
                    place_of_one.append([i, j])

                elif self.board_of_numbers[i][j] == 2:
                    place_of_two.append([i, j])

                else:
                    continue

        new_words = []
        buffer_word = ""
        row_col_buff = []
        # checking rows
        # Nie wiem czy te i, j dodawane do row_col_buff musi być szczerze...
        for i in range(len(copy_board)):
            for j in range(len(copy_board)):

                if j != 14:

                    if copy_board[i][j] != "-" and len(buffer_word) == 0:
                        buffer_word += copy_board[i][j]
                        row_col_buff.append([self.board_of_numbers[i][j]])

                    elif copy_board[i][j] != "-" and len(buffer_word) != 0:
                        buffer_word += copy_board[i][j]
                        row_col_buff.append([self.board_of_numbers[i][j]])

                    elif copy_board[i][j] == "-" and len(buffer_word) == 1:
                        buffer_word = ""
                        row_col_buff = []

                    elif copy_board[i][j] == "-" and len(buffer_word) > 1:
                        new_words.append([buffer_word, row_col_buff])
                        buffer_word = ""
                        row_col_buff = []

                    else:
                        continue

                else:

                    if copy_board[i][j] == "-" and len(buffer_word) <= 1:
                        buffer_word = ""
                        row_col_buff = []

                    elif copy_board[i][j] != "-" and len(buffer_word) >= 1:
                        buffer_word += copy_board[i][j]
                        row_col_buff.append([self.board_of_numbers[i][j]])
                        new_words.append([buffer_word, row_col_buff])
                        buffer_word = ""
                        row_col_buff = []

                    elif copy_board[i][j] == "-" and len(buffer_word) > 1:
                        new_words.append([buffer_word, row_col_buff])
                        buffer_word = ""
                        row_col_buff = []

                    else:
                        buffer_word = ""
                        row_col_buff = []
                        # End of inside loop

        # To check if actually put letters are in correct place
        checking_word = []
        for word in new_words:
            # Only used for first time during the looping
            if not checking_word:
                pass

            else:
                # correct option
                if 1 in checking_word and 2 not in checking_word:
                    checking_word = []

                else:
                    print("Letters put on the board are not in the correct place on the board")
                    # Pomyśleć nad loggerami
                    return False
            # Jak usuniemy i, j z row_col to też musimy zmienić tu indeksy | Juz pomyslelismy nad tym i weszlo w zycie
            for j in word[1]:
                checking_word.append(j[0])

        return True

    # Ewentualnie mozemy zmodyfikować to pod kopie board'u
    def check_words_from_board(self, loaded_dictionary: dict, copy_board: list_of_lists) -> bool:


        # Columns
        columns = list(zip(*copy_board))

        # Check rows
        """for i in range(len(copy_board)):
            str_row = "".join(copy_board[i])
            list_empty_words = str_row.split('-')
            filter_words = set(
                filter(lambda x: x != "" and len(x) >= 2 and x not in self.checked_words, list_empty_words))
            for j in filter_words:

                if j not in self.checked_words:

                    if Word().check_validity_of_word(j, loaded_dictionary) == True:
                        self.checked_words.add(j)
                        continue


                    else:
                        print("Unfortunately the word: \"{}\" hasn't been found in the dictionary".format(j))
                        return False

                else:
                    print("The word: \"{}\" has been already played".format(j))
                    return False

        # Check columns
        for i in range(len(copy_board)):
            str_row = "".join(columns[i])
            list_empty_words = str_row.split('-')
            filter_words = set(
                filter(lambda x: x != "" and len(x) >= 2 and x not in Board.checked_words, list_empty_words))

            for j in filter_words:

                if j not in self.checked_words:

                    if Word().check_validity_of_word(j, loaded_dictionary) == True:
                        # To jest zainicijalizowana zmienna
                        self.checked_words.add(j)
                        continue


                    else:
                        print("Unfortunately the word: \"{}\" hasn't been found in the dictionary".format(j))
                        return False

                else:
                    print("The word: \"{}\" has been already played".format(j))
                    return False

        # The board is valid
        return True"""
        # check rows
        for index_row, row in enumerate(copy_board):
            word_buffer = ""
            word_coords_buffer = []
            i_column = 0
            # chyba 13naście jednak
            while i_column < 14:
                word_buffer = ""
                word_coords_buffer = []
                if row[i_column] != '-' and row[i_column + 1] != '-':
                    while row[i_column] != '-':
                        word_buffer += row[i_column]
                        word_coords_buffer.append([index_row, i_column])
                        i_column += 1

                    if word_buffer not in self.checked_words.keys() and \
                            Word().check_validity_of_word(word_buffer, loaded_dictionary) == True:
                        # {WORD: [[[1,2],[3,4]]],...} len(WORD) == 1; len(WORD)[0] == 2;
                        self.checked_words.update({word_buffer: word_coords_buffer})

                    else:
                        print("The word has been already played or hasn't been found in dictionary 1")
                        return False

                else:
                    i_column += 1

        for index_column, column in enumerate(columns):
            word_buffer = ""
            word_coords_buffer = []
            i_row = 0
            while i_row < 14:
                word_buffer = ""
                word_coords_buffer = []
                # try do wyrzucenia bo iterujemy do 13
                if column[i_row] != '-' and row[i_row + 1] != '-':
                    while column[i_row] != '-':
                        word_buffer += column[i_row]
                        word_coords_buffer.append([i_row, index_column])
                        i_row += 1

                    if word_buffer not in self.checked_words.keys() and \
                            Word().check_validity_of_word(word_buffer, loaded_dictionary) == True:

                        self.checked_words.update({word_buffer: word_coords_buffer})

                    else:
                        print("The word has been already played or hasn't been found in dictionary 2")
                        return False
                else:
                    i_row += 1

        return True


"""   # rack moze byc bledem w interpreterze
    # To nie jest do końca word, bo prawie zawsze dokladamy litery do jakiegoś słowa
    # Sprawdzana też tu jest długość tablicy względem zagranego słowa
    def try_word(self, word: list, player: Player, rack: Rack, row_first_letter: int, column_first_letter: int) -> bool:
        # IF var_board will be accepted then we are going turn var_board into self.actual_board
        var_board = copy.deepcopy(self.actual_board)
        direction = direction.lower()
        word_length = len(word)"""

"""
# Miałoby tu być jeszcze direction
if (row_first_letter + word_length) > 14 or (column_first_letter + word_length) > 14:
            print("Length of the word due to placement is out of the board")
            return False

        if direction == "down":
            var_row_letter = row_first_letter
            for i in range(word_length):
                # "-" means empty cell
                if var_board[var_row_letter][column_first_letter] == "-":
                    var_board[var_row_letter][column_first_letter] = word[i]
                else:
                    print("Letter overlap the cell which is already taken by another letter")
                    return False
                # Because we are going towards the bottom...
                var_row_letter -= 1
                # DO UZUPELNIENIA

        elif direction == "right":
            var_col_letter = column_first_letter
            for i in range(word_length):
                if var_board[var_col_letter][column_first_letter] == "-":
                    var_board[row_first_letter][var_col_letter] = word[i]
                else:
                    print("Letter overlap the cell which is already taken by another letter")
                    return False

                # Because we are going towards the right side...
                var_col_letter += 1

        if direction == "down":"""