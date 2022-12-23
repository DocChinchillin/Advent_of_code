import time
import re


def main():

    with open('input') as f:
        lines = f.read().splitlines()

    mon = dict()
    for line in lines:
        key, val = line.split(': ')
        mon[key] = val

    eq = 'root'
    while re.search("[a-z]", eq):
        for k, i in mon.items():
            eq = eq.replace(k, '('+i+')')

    eval('print('+eq+')')


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}")
