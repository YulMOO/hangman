__author__ = 'user'

import unittest
import hangman

class hangmanTestCase(unittest.TestCase):

    def test_correct(self):
        answer = hangman.checkCorrectAnswer('google', 'google')
        self.assertEqual(answer, True)

    def test_wrong(self):
        answer = hangman.checkWrongAnswer('google', 'banana')
        self.assertEqual(answer, True)

if __name__ == "__main__":
    unittest.main()