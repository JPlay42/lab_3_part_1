from math import gcd, lcm


class Rational:
    def __init__(self, numerator: int, denominator: int):
        if not isinstance(numerator, int):
            raise TypeError('numerator is not int')
        if not isinstance(denominator, int):
            raise TypeError('denominator is not int')
        if denominator == 0:
            raise ValueError('division by zero')
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator
        divisor = gcd(numerator, denominator)
        self.__numerator = numerator // divisor
        self.__denominator = denominator // divisor

    @property
    def value(self):
        return self.__numerator / self.__denominator

    def __add__(self, other):
        return self.__add_by_arguments(
            self.__numerator,
            self.__denominator,
            other.__numerator,
            other.__denominator
        )

    def __sub__(self, other):
        return self.__add_by_arguments(
            self.__numerator,
            self.__denominator,
            -other.__numerator,
            other.__denominator
        )

    def __mul__(self, other):
        return Rational(self.__numerator * other.__numerator,
                        self.__denominator * other.__denominator)

    def __truediv__(self, other):
        return Rational(self.__numerator * other.__denominator,
                        self.__denominator * other.__numerator)

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __eq__(self, other):
        return self.__denominator == other.__denominator and \
               self.__numerator == other.__numerator

    def __ne__(self, other):
        return self.__denominator != other.__denominator or \
               self.__numerator != other.__numerator

    @staticmethod
    def __add_by_arguments(numerator_1: int,
                           denominator_1: int,
                           numerator_2: int,
                           denominator_2: int):
        common_denominator = lcm(denominator_1, denominator_2)
        new_numerator_1 = common_denominator // denominator_1 * numerator_1
        new_numerator_2 = common_denominator // denominator_2 * numerator_2
        return Rational(new_numerator_1 + new_numerator_2, common_denominator)

    def __str__(self):
        return f'{self.__numerator}/{self.__denominator}'
