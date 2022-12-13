import time
import ast
from functools import cmp_to_key
from itertools import count


def cmpLists(l1, l2):

    for cmp in zip(l1, l2):
        l, r = cmp
        if type(l) is int and type(r) is int:
            if l > r:
                return -1
            if l < r:
                return 1

        if type(l) is int and type(r) is list:
            ret = cmpLists([l], r)
            if ret != 0:
                return ret

        if type(r) is int and type(l) is list:
            ret = cmpLists(l, [r])
            if ret != 0:
                return ret

        if type(r) is list and type(l) is list:
            ret = cmpLists(l, r)
            if ret != 0:
                return ret

    if len(l1) < len(l2):
        return 1
    if len(l1) > len(l2):
        return -1
    return 0


def main():

    with open('input') as f:
        lines = f.read().splitlines()
    mul = 1
    all = []
    for line in lines:
        if line == '':
            continue
        # string to list
        l1 = ast.literal_eval(line)
        all.append(l1)

    p1 = [[2]]
    p2 = [[6]]
    all.append(p1)
    all.append(p2)
    s = sorted(all, key=cmp_to_key(
        lambda item1, item2: cmpLists(item2, item1)))

    for i, a in zip(count(1), s):
        if a == p1 or a == p2:
            mul *= i

    print(mul)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}")
