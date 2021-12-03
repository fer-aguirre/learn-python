""" Testing the methods """

# Import modules
import unittest
from unittest import TestCase
from palindrome import is_palindrome
from prime_number import is_prime


class TestingFunctions(TestCase):
    """ Tests to know if the methods works well """
    
    def test_is_palindrome(self):
        """ Testing is_palindrome method """
        self.assertEqual(is_palindrome('Ligar es ser agil'), True)
        self.assertEqual(is_palindrome('ArepeRa'), True)
        self.assertEqual(is_palindrome('Esto no es un palindromo'), False)

    def test_is_prime(self):
        """ Testing is_prime method """
        self.assertEqual(is_prime(0), False)
        self.assertEqual(is_prime(1), False)
        self.assertEqual(is_prime(53), True)
        self.assertEqual(is_prime(23), True)


if __name__ == '__main__':
    unittest.main()