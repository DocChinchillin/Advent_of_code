import time

class Dice():
    def __init__(self, sides):
        self.sides = sides;
        self.index = 1;
        self.rollNumber = 0

    def roll(self):
        self.rollNumber += 1
        roll = self.index
        self.index += 1
        self.index = self.index % 100
        return roll

    def sumRoll3(self):
        sum = self.roll()
        sum += self.roll()
        sum += self.roll()
        return sum
        

def main():
    vrednost = {i:i for i in range(1,10)}
    vrednost[0] = 10

    index = [10,1]
    score = [0,0]

    kocka = Dice(100)
    ind = 0
    while True:
        index[ind] += kocka.sumRoll3()
        index[ind] = index[ind] % 10
        score[ind] += vrednost[index[ind]]
        if score[ind] >= 1000:
            break
        ind = 1 - ind

    print(score[1 - ind]*kocka.rollNumber)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'Time is : {end - start}') 