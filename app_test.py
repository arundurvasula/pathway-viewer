import os
import unittest
import tempfile

from app import app

class AppTestCase(unittest.TestCase):

	def test_index(self):
		test = app.test_client(self)
		rv = test.get('/')
		self.assertEqual(rv.status_code, 200)

	def test_one_gene(self):
		test = app.test_client(self)
		form = {'gene_names': "FLOT1"}
		rv = test.post('/data', data=form)
		assert "FLOT1" in rv.data

	def test_multiple_genes(self):
		test = app.test_client(self)
		form = {'gene_names': "FLOT1\nGALM"}
		rv = test.post('/data', data=form)
		print rv.data
		assert "Insulin signalling pathway" in rv.data


if __name__ == '__main__':
    unittest.main()