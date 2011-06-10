import problem1
import unittest

class TestProblem1(unittest.TestCase):
	
	def test_sum_to_10(self):
		self.assertEqual(problem1.sum_natural_numbers(10),23)
		
		
unittest.main()