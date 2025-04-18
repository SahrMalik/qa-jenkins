import requests
import unittest

class FlaskAppTests(unittest.TestCase):
    BASE_URL = "http://localhost:80"  # Added quotes

    def test_home_page(self):
        response = requests.get(f"{self.BASE_URL}/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Hello Sahr", response.text)
        self.assertIn("I'm currently running in", response.text)

if __name__ == "__main__":
    unittest.main()
