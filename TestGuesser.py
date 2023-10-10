# программа для тестирования модулей

import unittest

from guesser import Guesser

class TestGuesser(unittest.TestCase):
    
          
    def setUp(self):
            self.guesser = Guesser("word")    
    
    
    def test_case_init(self):
        print("\nTest 1 - __init__\n")
        test_word = "word"
        test_opened_word = ['?', '?', '?', '?']      
        self.assertEqual(test_word, self.guesser.word)
        self.assertEqual(test_opened_word, self.guesser.opened)
        print(test_word)
        print(self.guesser.word)
        print(test_opened_word)
        print(self.guesser.opened)
        print("\nFinished Test 1\n")
        pass

    def test_case_getOpened(self):
        print("\nTest 2 - getOpened\n")
        test_word = "word"
        test_opened_word = "????"        
        self.assertEqual(test_opened_word, self.guesser.get_opened())
        print(test_word)
        print(test_opened_word)
        print(self.guesser.opened)
        print("\nFinished Test 2\n")  
        pass

    def test_case_openChar(self):
        print("\nTest 3 - openChar\n")
        test_word = "word"
        test_opened_word = "????"        
        self.guesser.open_char('w')
        self.assertEqual(self.guesser.get_opened(), 'w???')
        self.guesser.open_char('o')
        self.assertEqual(self.guesser.get_opened(), 'wo??')
        print("\nFinished Test 3\n")
        pass
    
    def test_case_isGeussed(self):
            print("\nTest 4 - isGeussed\n")     
            self.assertEqual(self.guesser.is_geussed(), False)
            print(self.guesser.is_geussed())
            print("\nFinished Test 4\n")
            pass
    
    def test_case_getword(self):
        print("\nTest 5 - getWord\n")
        test_word = "word"        
        self.assertEqual(test_word, self.guesser.get_word())
        print(test_word)
        print(self.guesser.get_word())
        print("\nFinished Test 5\n")  
        pass

    def test_case_hasChar(self):
        print("\nTest 6 - hasChar\n")
        test_letter1 = "w"
        test_letter2 = "q"
        waited_result1 = True
        waited_result2 = False
        self.assertEqual(self.guesser.has_char(test_letter1), waited_result1)
        self.assertEqual(self.guesser.has_char(test_letter2), waited_result2)
        print(waited_result1)
        print(self.guesser.has_char(test_letter1))
        print(waited_result2)
        print(self.guesser.has_char(test_letter2))
        print("\nFinished Test 6\n")
        pass    

    if __name__ == "__main__":
        unittest.main(exit=False)