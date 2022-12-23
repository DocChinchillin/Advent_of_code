import time
import re
from sympy import symbols, solve


def main():

    with open('input') as f:
        lines = f.read().splitlines()

    mon = dict()
    for line in lines:
        key, val = line.split(': ')
        mon[key] = val

    eq = mon['root']
    eq: str
    eq = eq.replace("+", "-")
    while re.search("[a-z]", eq):
        for k, i in mon.items():
            if k == 'humn':
                eq = eq.replace(k, '(X)')
            else:
                eq = eq.replace(k, '('+i+')')

    x = symbols('X')
    print(solve(eq, x))


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}")
