#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
8. Поле first — целое число, левая граница диапазона, включается в диапазон; поле second —
целое число, правая граница диапазона, не включается в диапазон. Пара чисел
представляет полуоткрытый интервал [first, second). Реализовать метод rangecheck() —
проверку заданного целого числа на принадлежность диапазону.
"""


def is_number(a):
    try:
        float(a)
    except ValueError:
        return False
    return True


class Coordinates:
    def __init__(self, first=0.0, second=0.0):
        if is_number(first) and is_number(second):
            if first > 0 and second > 0:
                self.first = first
                self.second = second
            else:
                raise ValueError
        else:
            raise ValueError

    def read(self):
        self.first = float(input("Enter the first value: "))
        self.second = int(input("Enter the second value: "))

    def display(self):
        print(f"First value: {self.first}")
        print(f"Second value: {self.second}")

    def rangecheck(self, x):
        if self.first <= x < self.second:
            print(f"{x} принадлежит диапазону [{self.first},{self.second})")
        else:
            print(f"{x} не принадлежит диапазону [{self.first},{self.second})")


def make_coordinates(first, second):
    if is_number(first) and is_number(second) and first > 0 and second > 0:
        coordinates = Coordinates(first, second)
        return coordinates
    else:
        raise ValueError


if __name__ == '__main__':
    p = make_coordinates(2, 10)
    p.display()
    p.rangecheck(5)
    p.rangecheck(10)
    p.rangecheck(2)
