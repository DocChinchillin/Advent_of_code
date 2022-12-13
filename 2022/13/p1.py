import time
import ast
from itertools import count


def cmpLists(l1, l2):

    for cmp in zip(l1, l2):
        l, r = cmp
        if type(l) is int and type(r) is int:
            if l > r:
                return False
            if l < r:
                return True

        if type(l) is int and type(r) is list:
            ret = cmpLists([l], r)
            if ret is not None:
                return ret

        if type(r) is int and type(l) is list:
            ret = cmpLists(l, [r])
            if ret is not None:
                return ret

        if type(r) is list and type(l) is list:
            ret = cmpLists(l, r)
            if ret is not None:
                return ret
    if len(l1) < len(l2):
        return True
    if len(l1) > len(l2):
        return False
    return None


def main():

    with open('input') as f:
        lines = f.read().split('\n\n')
    sum = 0
    for i, line in zip(count(1), lines):
        l1, l2 = line.split('\n')[:2]
        # string to list
        l1 = ast.literal_eval(l1)
        l2 = ast.literal_eval(l2)
        if cmpLists(l1, l2):
            sum += i

    print(sum)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}")
