import problem3
import unittest

class TestProblem3(unittest.TestCase):
	
	def test(self):
		self.assertEqual(problem3.prime_factorise(13195),[5,7,13,29])
		
		
unittest.main()