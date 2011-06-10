import problem5
import unittest

class TestProblem5(unittest.TestCase):
	
	def test(self):
		self.assertEqual(problem5.lcm(1,10),2520)
		
		
unittest.main()