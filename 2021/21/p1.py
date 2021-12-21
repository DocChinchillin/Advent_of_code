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

    p1_index = 10
    p2_index = 1

    p1_score = 0
    p2_score = 0

    kocka = Dice(100)
    
    while p1_score <= 1000 and p2_score <=1000:
        p1_index += kocka.sumRoll3()
        p1_index = p1_index % 10
        p1_score += vrednost[p1_index]

        if p1_score > 1000:
            break

        p2_index += kocka.sumRoll3()
        p2_index = p2_index % 10
        p2_score += vrednost[p2_index]
    
    if p1_score > 1000:
        print(p2_score*kocka.rollNumber)
    else:
        print(p1_score*kocka.rollNumber)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'Time is : {end - start}') 