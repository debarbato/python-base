#!/usr/bin/env python3
"""Imprime a tabuada do 1 ao 10 """
__version__ = "0.1.0"
__author__ = "David"


base = [1,2,3,4,5,6,7,8,9,10]
print(base)
print(type(base))
numeros = list(range(1,11))

# Iterable (percorrer)
for numero in numeros:
    print("Tabuada do:", numero)
    for outro_numero in numeros:
        print(numero, "X", outro_numero, "=",  outro_numero * numero)
