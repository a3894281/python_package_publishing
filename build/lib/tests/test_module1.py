import unittest
from main_code.module1 import add, sub


class TestModule1(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(1, -1), 0)
        
    def test_sub(self):
        self.assertEqual(sub(1, 2), -1)
        self.assertEqual(sub(4, 2), 2)
        

if __name__ == "__main__":
    unittest.main()