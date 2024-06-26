import unittest
from terme import Terme
from fraction import Fraction
from solver import Solver
class TestTerme(unittest.TestCase):

    def test_sum_terme(self):
        a = Terme(5,"x",1)
        b = Terme(2,"x",1)
        self.assertEqual(a + b, Terme(7,"x", 1))

    def test_sum_multiple_terms(self):
        a = Terme(5,"x",1)
        b = Terme(2,"x", 1)
        c = Terme(3,"x", 1)
        self.assertEqual(a + b + c , Terme(10, "x", 1))

    def test_subtract_terme(self):
        a = Terme(5,"x",1)
        b = Terme(2,"x", 1)
        self.assertEqual(a - b, Terme(3,"x", 1))

    def test_multiply_terme(self):
        a = Terme(5,"x",1)
        b = Terme(2,"x", 2)
        self.assertEqual(a*b, Terme(10,"x",3))

    def test_multiply_different_terms(self):
        a = Terme(5, "x", 1)
        b = Terme(2, "y", 2)
        self.assertEqual(a*b, Terme(10,"xy", 3))

    def test_division_terme(self):
        a = Terme(4,"x",1)
        b = Terme(2,"x", 2)
        self.assertEqual(a/b, Terme(2,"x",-1))

class TestFraction(unittest.TestCase):
    def test_pgcm(self):
        self.assertEqual(Fraction.PGCD(30, 12), 6)

    def test_simplify_fraction(self):
        self.assertEqual(Fraction(30,12).simplify(), Fraction(5, 2))

    def test_add_fraction_with_same_denominator(self):
        self.assertEqual(Fraction(1,4) + Fraction(2, 4), Fraction(3,4))

    def test_add_fraction_with_different_denominator(self):
        self.assertEqual(Fraction(1,4) + Fraction(1,2), Fraction(3,4))

    def test_multiply_fraction(self):
        self.assertEqual(Fraction(1,4)*Fraction(1, 2), Fraction(1,8))

    def test_divide_fraction(self):
        self.assertEqual(Fraction(1,4)/Fraction(1, 2), Fraction(1,2))

class TestFractionsandTerme(unittest.TestCase):
    def test_sum_terme(self):
        a = Terme(Fraction(4,3), "x", 1)
        b = Terme(Fraction(2), "x", 1)
        self.assertEqual(a + b, Terme(Fraction(10,3), "x", 1))

    def test_sum_multiple_terms(self):
        a = Terme(Fraction(2,5), "x", 1)
        b = Terme(Fraction(20,5), "x", 1)
        c = Terme(Fraction(3), "x", 1)
        self.assertEqual(a + b + c, Terme(Fraction(37,5), "x", 1))

    def test_subtract_terme(self):
        a = Terme(Fraction(1,2), "x", 1)
        b = Terme(Fraction(1,4), "x", 1)
        self.assertEqual(a - b, Terme(Fraction(1,4), "x", 1))

    def test_multiply_terme(self):
        a = Terme(Fraction(3,4), "x", 1)
        b = Terme(Fraction(1,8), "x", 2)
        self.assertEqual(a * b, Terme(Fraction(3,32), "x", 3))

    def test_multiply_different_terms(self):
        a = Terme(Fraction(2,3), "x", 1)
        b = Terme(Fraction(1,5), "y", 2)
        self.assertEqual(a * b, Terme(Fraction(2,15), "xy", 3))

    def test_division_terme(self):
        a = Terme(Fraction(1,2), "x", 1)
        b = Terme(Fraction(1,4), "x", 2)
        self.assertEqual(a / b, Terme(Fraction(2,1), "x", -1))
class TestSolver(unittest.TestCase):
    def testsolverdegreeone(self):
        solver = Solver()
        self.assertEqual(solver.solve([Terme(5,"x",1), Terme(-15,"x",0)]), 3)

if __name__ == '__main__':
    unittest.main()