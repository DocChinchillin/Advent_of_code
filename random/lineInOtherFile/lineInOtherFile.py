import sys


def main(file1, file2):
    with open(file1) as f:
        lines1 = f.read().splitlines()

    with open(file2) as f:
        lines2 = f.read().splitlines()

    numDiffs = 0

    for n, line in enumerate(lines1):
        if line not in lines2:
            print(f"Diff on line {n + 1}: {line} ")
            numDiffs += 1

    print(f"Found {numDiffs} different lines")


if __name__ == "__main__":
    if len(sys.argv[1:]) < 2:
        print("Provide 2 files example: python lineInOtherFile.py testInput solutionInput")
    else:
        main(sys.argv[1], sys.argv[2])
