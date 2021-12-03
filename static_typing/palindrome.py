# Python module to know if a string is palindrome

# Fuction receive a string and return a bool
def is_palindrome(string: str) -> bool:  
    # Delete whitespaces and convert to lowers
    string = string.replace(' ', '').lower()
    # Reverse a string
    return string == string[::-1]

def run():
    print(is_palindrome(1000))

# Install mypy module:
# $pip3 install mypy
# Run in terminal:
# $mypy palindrome.py --check-untyped-defs

if __name__ == '__main__':
    run()