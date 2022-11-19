import unittest

from task1.src.rational import Rational


class RationalTest(unittest.TestCase):
    __small = Rational(1, 2)
    __big = Rational(3, 4)

    def test_validation(self):
        number = Rational(1, 2)
        self.assertEqual(0.5, number.value)
        with self.assertRaises(TypeError):
            Rational(1.5, 2)
        with self.assertRaises(TypeError):
            Rational(2, 1.5)
        with self.assertRaises(ValueError):
            Rational(3, 0)

    def test_str(self):
        self.assertEqual('1/2', str(Rational(1, 2)))
        self.assertEqual('-3/4', str(Rational(-3, 4)))
        self.assertEqual('-5/6', str(Rational(5, -6)))
        self.assertEqual('1/8', str(Rational(128, 1024)))

    def test_add(self):
        number = Rational(1, 4) + Rational(1, 2)
        self.assertEqual(0.75, number.value)
        self.assertEqual('3/4', str(number))

    def test_sub(self):
        number = Rational(1, 4) - Rational(1, 2)
        self.assertEqual(-0.25, number.value)
        self.assertEqual('-1/4', str(number))

    def test_mul(self):
        number = Rational(1, 2) * Rational(-3, 4)
        self.assertEqual(-0.375, number.value)
        self.assertEqual('-3/8', str(number))

    def test_div(self):
        number = Rational(3, 4) / Rational(-1, 2)
        self.assertEqual(-1.5, number.value)
        self.assertEqual('-3/2', str(number))

    def test_less_than(self):
        self.assertTrue(self.__small < self.__big)
        self.assertFalse(self.__big < self.__small)
        self.assertFalse(self.__small < self.__small)
        self.assertFalse(self.__big < self.__big)

    def test_less_or_equal(self):
        self.assertTrue(self.__small <= self.__big)
        self.assertFalse(self.__big <= self.__small)
        self.assertTrue(self.__small <= self.__small)
        self.assertTrue(self.__big <= self.__big)

    def test_greater_than(self):
        self.assertFalse(self.__small > self.__big)
        self.assertTrue(self.__big > self.__small)
        self.assertFalse(self.__small > self.__small)
        self.assertFalse(self.__big > self.__big)

    def test_greater_or_equal(self):
        self.assertFalse(self.__small >= self.__big)
        self.assertTrue(self.__big >= self.__small)
        self.assertTrue(self.__small >= self.__small)
        self.assertTrue(self.__big >= self.__big)

    def test_equal(self):
        self.assertFalse(self.__small == self.__big)
        self.assertFalse(self.__big == self.__small)
        self.assertTrue(self.__small == self.__small)
        self.assertTrue(self.__big == self.__big)

    def test_not_equal(self):
        self.assertTrue(self.__small != self.__big)
        self.assertTrue(self.__big != self.__small)
        self.assertFalse(self.__small != self.__small)
        self.assertFalse(self.__big != self.__big)


if __name__ == '__main__':
    unittest.main()
