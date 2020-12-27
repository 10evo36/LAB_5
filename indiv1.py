#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


# Ввести список А из 10 элементов, найти произведение положительных элементов и вывести
# его на экран.
if __name__ == '__main__':
    A = list(map(int, input("Ввести список А из 10 элементов:").split()))
    if len(A) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)

    S = 1
    b = [i for i in A if i > 0]
    for i in b:
        S *= i

    print(f'Произведение положительных частей списка равно {S}')