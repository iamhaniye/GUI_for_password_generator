from abc import ABC , abstractmethod
import random
import string
import nltk
nltk.download('words')


class PasswordGenerator(ABC):
    
    @abstractmethod
    def generate(self):
        pass
    



class PinGenerator(PasswordGenerator):

    def __init__(self,length = 4):
        self.length = length


    def generate(self):
        return("".join(random.choice(string.digits) for _ in range(self.length))) 




class RandomPasword(PasswordGenerator):
    def __init__(self, length = 8 ,  include_number = False , include_symbol = False ):

        self.character = string.ascii_letters

        if include_number:
            self.character += string.digits
        
        if include_symbol:
            self.character += string.punctuation

        self.length = length
        self.include_number = include_number
        self.include_symbol = include_symbol

    
    def generate(self):
        return("".join(random.choice(self.character) for _ in range(self.length)))

        


class MemorablePassword(PasswordGenerator):
    def __init__(self, num_of_words = 4, word_list = None ):

        self.num_of_words = num_of_words

        if word_list is None:
            self.word_list = nltk.corpus.words.words()
        else:
            self.word_list = word_list
        
        


    def generate(self):

        return("-".join(random.choice(self.word_list) for _ in range(self.num_of_words)))

