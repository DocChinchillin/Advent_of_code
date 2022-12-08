import time


def main():

    with open('input') as f:
        lines = f.read().splitlines()

    line = lines[0]
    for n in range(len(line)-13):
        s = set(line[n:n+14])
        if len(s) == 14:
            # zanima nas zadnji znak, ki smo ga rabli
            print(n + 14)
            break


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}")
