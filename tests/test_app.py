import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestApp(unittest.TestCase):
    def test_file_existence(self):
        self.assertTrue(os.path.exists('app.py'))
        self.assertTrue(os.path.exists('calculator.py'))

    def test_calculator_import(self):
        try:
            from calculator import SimpleCalculator
            calc = SimpleCalculator()
            self.assertTrue(hasattr(calc, 'add'))
            self.assertTrue(hasattr(calc, 'subtract'))
            self.assertTrue(hasattr(calc, 'multiply'))
            self.assertTrue(hasattr(calc, 'divide'))
        except ImportError as e:
            self.fail(f"Import error: {e}")

if __name__ == '__main__':
    unittest.main()