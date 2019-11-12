from app import app 
import unittest

class AppTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_fortune_results_default_response(self):
        result = self.app.get('/fortune_results')
        self.assertIn('Good luck.', str(result.data))

    def test_fortune_results_bear(self):
        result = self.app.get('/fortune_results?animal=Bear')
        self.assertIn("You'll have good luck for 10 years!", str(result.data))
    
    def test_fortune_results_whale(self):
        result = self.app.get('/fortune_results?animal=Whale')
        self.assertIn("You'll have a magical day!", str(result.data))

# run the tests
if __name__ == '__main__':
    unittest.main()