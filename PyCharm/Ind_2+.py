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

    def read(self):
        time_str = input("Введите время в формате 'час:минута:секунда': ")
        hour, minute, second = map(int, time_str.split(":"))
        self.hour = hour
        self.minute = minute
        self.second = second

    def display(self):
        print("{:02d}:{:02d}:{:02d}".format(self.hour, self.minute, self.second))

    def from_seconds(self, seconds):
        hour = seconds // (60*60)
        minute = (seconds // 60) % 60
        second = seconds % 60
        return self(hour, minute, second)

    def from_time(self, time):
        return self(time.hour, time.minute, time.second)

    def from_string(self, time_str):
        hour, minute, second = map(int, time_str.split(":"))
        return self(hour, minute, second)

    def to_seconds(self):
        seconds = self.hour * 60 * 60
        seconds += self.minute * 60
        seconds += self.second
        return seconds

    def to_minutes(self):
        return round(self.to_seconds() / 60)

    def add_seconds(self, seconds):
        total_seconds = self.to_seconds() + seconds
        return Time.from_seconds(total_seconds)

    def subtract_seconds(self, seconds):
        total_seconds = self.to_seconds() - seconds
        return Time.from_seconds(total_seconds)

    def diff_in_seconds(self, other):
        current_seconds = self.to_seconds()
        other_seconds = other.to_seconds()
        return abs(current_seconds - other_seconds)

    def is_equal(self, other):
        return self.hour == other.hour and self.minute == other.minute and self.second == other.second

    def is_greater(self, other):
        current_seconds = self.to_seconds()
        other_seconds = other.to_seconds()
        return current_seconds > other_seconds

    def is_less(self, other):
        current_seconds = self.to_seconds()
        other_seconds = other.to_seconds()
        return current_seconds < other_seconds