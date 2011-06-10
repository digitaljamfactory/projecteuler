import problem2
import unittest

class TestProblem2(unittest.TestCase):
	
	def test(self):
		self.assertEqual([num for num in problem2.even_valued_fib_numbers(50)],[0,2,8,34])
		
		
unittest.main()