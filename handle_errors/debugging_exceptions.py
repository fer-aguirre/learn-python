def divisor(num):
    divisors = []
    if num <= 0:
        raise ValueError('No se pueden ingresar 0 ni números negativos')
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    try:
        num = int(input('Ingresa un número: '))
        print(divisor(num))
    except ValueError:
        print('Debes ingresar un número positivo')



if __name__ == '__main__':
    run()
