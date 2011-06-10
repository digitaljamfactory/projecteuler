import problem6
import unittest

class TestProblem6(unittest.TestCase):
	
	def test_sum_of_squares(self):
		self.assertEqual(problem6.sum_of_squares(11),385)
	
	def test_square_of_sums(self):
		self.assertEqual(problem6.square_of_sums(11),3025)
		
	def test_difference(self):
		self.assertEqual(problem6.difference_sum_of_squares_and_square_of_sums(11),2640)
		
		
unittest.main()