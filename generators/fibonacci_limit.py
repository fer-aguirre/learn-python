"""
Función que implementa un generador
de la sucesión de Fibonacci
a partir de un máximo de valores
definido por el usuario
"""

import time

def fibo_gen():
    n1 = 0
    n2 = 1
    counter = 0
    max = int(input('Ingresa el máximo de valores para la sucesión de Fibonacci: '))
    assert max > 1, "El valor debe ser mayor que 1"
    while max > 1:
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
    fibonacci = fibo_gen()
    for element in fibonacci:
        print(element)
        time.sleep(0.5)
