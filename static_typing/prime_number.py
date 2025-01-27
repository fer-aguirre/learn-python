""" Python module to know if a number is prime """

# Fuction receive an int and return a bool
def is_prime(number: int) -> bool:
    result = [x for x in range(2, number) if number % x == 0]
    return len(result) == 0 and number > 1

def run():
    number = int(input("Ingresa un número primo: "))
    #number = "4"
    print(is_prime(number))

"""
Install mypy module:
$ pip3 install mypy
Run in terminal:
$ mypy prime_number.py --check-untyped-defs
"""


if __name__ == '__main__':
    run()