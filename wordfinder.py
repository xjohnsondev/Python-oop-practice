"""Word Finder: finds random words from a dictionary."""
import random
FILE = "words.txt"

class WordFinder:
    
    def __init__(self):
        self.f = open(FILE, "r")
        self.count_words()
        
    def count_words(self):
        self.data = self.f.readlines()
        print(f"{len(self.data)} words read")

    def random(self):
        line = random.choice(self.data)
        print(line)


class SpecialWordFinder(WordFinder):

    def __init__(self):
        super().__init__()
        self.special_word()

    def special_word(self):
        [w.strip() for w in self.f
                if w.strip() and not w.startswith("#")]


w = WordFinder()
w.random()

s = SpecialWordFinder()
