#!/usr/bin/env python3
"""Imprime a tabuada do 1 ao 10 """
__version__ = "0.1.1"
__author__ = "David"

#print(base)
#print(type(base))
numeros = list(range(1,11))

# Iterable (percorrer)
# for numero in numeros:
    # print("Tabuada do:", numero)
    # for outro_numero in numeros:
        # print(numero, "X", outro_numero, "=",  outro_numero * numero)

for n1 in numeros:
    print('{:-^21}'.format(f"Tabuada do {n1}"))
    print()
    for n2 in numeros:
        resultado = n1 * n2
        print("{:^18}".format(f"{n1} x {n2} = {resultado}"))
    print(30*'#')












