import unittest
from suggest import *

class MyTests(unittest.TestCase):
	def setUp(self):
		self.sug = Suggester(SUGGEST_FILE)

	def test_len_answer(self):
		answer = self.sug.get('т')
		self.assertEqual(len(answer), 10)

	def test_startswith_rus_t(self):
		answer = self.sug.get('т')
		for ans in answer:
			self.assertEqual(ans[:1], 'т')

	def test_startswith_rus_a(self):
		answer = self.sug.get('а')
		self.assertEqual(answer[0], 'а')

unittest.main()
