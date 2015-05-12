import os
import unittest
import tempfile

from app import app

class AppTestCase(unittest.TestCase):

	def test_index(self):
		test = app.test_client(self)
		rv = test.get('/')
		self.assertEqual(rv.status_code, 200)


if __name__ == '__main__':
    unittest.main()