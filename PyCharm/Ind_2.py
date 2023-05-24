#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
8. Создать класс Time для работы со временем в формате «час:минута:секунда». Класс
должен включать в себя не менее четырех функций инициализации: числами, строкой
(например, «23:59:59»), секундами и временем. Обязательными операциями являются:
вычисление разницы между двумя моментами времени в секундах, сложение времени и
заданного количества секунд, вычитание из времени заданного количества секунд,
сравнение моментов времени, перевод в секунды, перевод в минуты (с округлением до
целой минуты).

"""


class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def read_str(self):
        time_str = input("Введите время в формате ЧЧ:ММ:СС: ")
        try:
            self.hour, self.minute, self.second = map(int, time_str.split(":"))
        except ValueError:
            print("Ошибка: время должно быть в формате ЧЧ:ММ:СС")
            exit(1)

    def read_sec(self):
        time_str = int(input("Введите время в секундах:"))
        try:
            self.hour = time_str // 3600
            self.minute = (time_str % 3600) // 60
            self.second = (time_str % 3600) % 60
        except ValueError:
            print("Ошибка: время должно быть в секундах.")
            exit(1)

    def display(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

    def to_seconds(self):
        return self.hour * 3600 + self.minute * 60 + self.second

    def to_minutes(self):
        return round(self.to_seconds() / 60)

    def diff_seconds(self, other):
        return abs(self.to_seconds() - other.to_seconds())

    def add_seconds(self, sec):
        total_sec = self.to_seconds() + sec
        self.hour = total_sec // 3600
        self.minute = (total_sec % 3600) // 60
        self.second = total_sec % 60

    def sub_seconds(self, sec):
        total_sec = self.to_seconds() - sec
        self.hour = total_sec // 3600
        self.minute = (total_sec % 3600) // 60
        self.second = total_sec % 60

    def eq(self, other):
        current_seconds = self.to_seconds()
        other_seconds = other.to_seconds()
        if current_seconds > other_seconds:
            return f"{self.display()} > {other.display()}"
        elif current_seconds < other_seconds:
            return f"{self.display()} < {other.display()}"
        else:
            return f"{self.display()} = {other.display()}"


if __name__ == '__main__':
    t1 = Time(12, 00, 00)
    t2 = Time()
    t2.read_str()
    print(f"t1: {t1.display()}")
    print(f"t2: {t2.display()}")

    print(t1.to_seconds())

    t3 = Time()
    t3.read_sec()
    print(f"t3: {t3.display()}")
    t4 = Time(12, 40, 00)

    print(t1.eq(t4))



    # delta_sec = t1.diff_seconds(t2)
    # print(f"Разница между временами: {delta_sec} секунд")
    #
    # t1.add_seconds(120)
    # print(f"t1 + 120 секунд: {t1.display()}")
    #
    # t2.sub_seconds(300)
    # print(f"t2 - 300 секунд: {t2.display()}")
