import unittest
from terme import Terme
class TestTerme(unittest.TestCase):

    def test_sum_terme(self):
        a = Terme(5,"x",1)
        b = Terme(2,"x",1)
        self.assertEqual(a + b, Terme(7,"x", degree=1))

    def test_subtract_terme(self):
        a = Terme(5,"x",1)
        b = Terme(2,"x", 1)
        self.assertEqual(a - b, Terme(3,"x", 1))

    def test_multiply_terme(self):
        a = Terme(5,"x",1)
        b = Terme(2,"x", 2)
        self.assertEqual(a*b, Terme(10,"x",3))

    def test_division_terme(self):
        a = Terme(4,"x",1)
        b = Terme(2,"x", 2)
        self.assertEqual(a/b, Terme(2,"x",-1))


if __name__ == '__main__':
    unittest.main()