import os
import numpy as np


class Word:
    # Mialo być WORD w parametrach
    # W tym momencie klasa Word musi zostać wywołana na początku programu, żeby miała załadowane zmienne
    """def __init__(self):
        # Najprawdopodobniej do wyjebania metoda upper()
        #self.word = word.upper()
        # Numpy arrays. We are loading here words from our divided dict
        # {'A': ["First_A_word"... "Last_A_word"], 'B': ["First_B_word"... ,"Last_B_Word"]...}
        self.loaded_dictionary = {}
        for i in range(65, 91):
            letter = "{}".format(chr(i))
            try:
                self.loaded_dictionary.update({letter: np.genfromtxt(Word.get_path_for_divided(chr(i)), dtype=str)})
            except Exception as e:
                print("This txt file: {}.txt doesn't exist in this directory".format(chr(i)))"""

    # Straight checking word in the file
    # Do wyjebania
    """def check_validity_of_word(self) -> bool:
        # wpierw potrzebujemy uprządkowanych slownikow, ktore zaczynają się od litery słowa...
        first_letter = self.word[0]
        with open(Word.get_path_for_divided(first_letter)) as reader:
            for line in reader:
                if line == self.word:
                    return True

        return False"""

    @staticmethod
    def get_the_dictionary_for_words() -> dict:
        """The purpose of this method is to load """
        loaded_dictionary = {}
        for i in range(65, 91):
            letter = "{}".format(chr(i))
            try:
                loaded_dictionary.update({letter: np.genfromtxt(Word.get_path_for_divided(chr(i)), dtype=str)})
            except Exception as e:
                print("{}.txt doesn't exist in this directory".format(chr(i)))

        return loaded_dictionary

    @staticmethod
    def check_validity_of_word(word: str, loaded_dictionary: dict) -> bool:
        word = word.upper()
        letter = word[0]
        if word in loaded_dictionary.get(letter):
            return True

        else:
            return False

    # It is the path to the specific file depending on the first letter of the word
    # @staticmethod
    @staticmethod
    def get_path_for_divided(starting_letter: str) -> str:
        path_of_main_dict = "{}{}".format(os.getcwd(), "\\dict_for_game")
        return "".join([path_of_main_dict, "\\divided_dict", "\\", starting_letter, ".txt"])
