import problem4
import unittest

class TestProblem3(unittest.TestCase):
	
	def test(self):
		self.assertEqual(problem4.find_largest_palindrome(10,100),9009)
		
		
unittest.main()