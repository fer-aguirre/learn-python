"""
A function that deploys a 
generator of Fibonacci sequence
from a maximum value
entered by the user
"""

import time

def fibo_gen(max):
    n1 = 0
    n2 = 1
    counter = 0
    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter +=1
            yield n2
        else:
            aux = n1 + n2
            # Swapping
            n1, n2 = n2, aux
            counter += 1
            if aux <= max:
                yield aux
            else:
                break



if __name__ == '__main__':
    max = input('Ingresa el máximo de valores para la sucesión de Fibonacci: ')
    assert max.isnumeric() and int(max) >= 1, "El valor debe ser un número positivo"
    fibonacci = fibo_gen(int(max))
    for element in fibonacci:
        print(element)
        time.sleep(0.5)
