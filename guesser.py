# программа с ядром игры

class Guesser:
    def __init__(self, word):
        self.word = word
        self.opened = ['?' for _ in range(len(word))]
        
    def is_geussed(self):
        return None
        
    def open_char(self, char):
        for i in range(len(self.word)):
            if self.word[i] == char:
                self.opened[i] = self.word[i]
        
    def get_opened(self):
        return ''.join(self.opened)
        
    def get_word(self):
        return None
        
    def has_char(self, char):
        return None
        