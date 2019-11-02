import unittest
import rpn

class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate('1 1 +')
		self.assertEqual(2, result)
	def test_sub(self):
		result = rpn.calculate('5 3 -')
		self.assertEqual(2, result)
	def test_multi(self):
		result = rpn.calculate('12 3 *')
		self.assertEqual(36, result)
	def test_divide(self):
		result = rpn.calculate('16 3 /')
		self.assertEqual(5, result)
	def test_divide1(self):
		result = rpn.calculate('16 4 /')
		self.assertEqual(4, result)
	def test_mod(self):
		result = rpn.calculate('16 3 %')
		self.assertEqual(1, result)
	def test_badinput(self):
		with self.assertRaises(TypeError):
			result = rpn.calculate('1 2 3 +')
