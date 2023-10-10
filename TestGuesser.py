# программа для тестирования модулей

import unittest

from guesser import Guesser

class TestGuesser(unittest.TestCase):
    
    
    test_word = "word"
    test_opened_word = "????"    
    
    
    def test_case_init(self):
        print("\nTest 1 - __init__\n")
        self.guesser = Guesser(test_word)
        self.assertEqual(test_word, self.guesser.word)
        self.assertEqual(test_opened_word, self.guesser.opened)
        print(test_word)
        print(self.guesser.word)
        print(test_opened_word)
        print(self.guesser.opened)
        print("\nFinished Test 1\n")        

    def test_case_getOpened(self):
        print("\nTest 2 - getOpened\n")
        self.assertEqual(test_opened_word, self.guesser.get_opened())
        print(test_word)
        print(test_opened_word)
        print(self.guesser.opened)
        print("\nFinished Test 2\n")        

    def test_case_openChar(self):
        print("\nTest 3 - openChar\n")
        self.guesser.open_char('w')
        self.assertEqual(self.guesser.get_opened(), 'w???')
        self.guesser.open_char('o')
        self.assertEqual(self.guesser.get_opened(), 'wo??')
        print("\nFinished Test 3\n")

    if __name__ == "__main__":
        unittest.main()