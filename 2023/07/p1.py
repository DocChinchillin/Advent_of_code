import time
from collections import Counter

CARDS = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}


class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = int(bid)
    
    def __str__(self):
        return f"{self.cards}"
    
    def getType(self):
        count = Counter(self.cards)
        com = count.most_common(2)

        n = com[0][1]
        if len(com) > 1:
            m = com[1][1]
        else:
            m = 0
        if n == 5:
            return 7
        if n == 4:
            return 6
        if n == 3 and m == 2:
            return 5
        if n == 3 and m == 1:
            return 4
        if n == 2 and m == 2:
            return 3
        if n == 2 and m == 1:
            return 2
        return 1
        
            
        
    
    def __lt__(self, other):
        s = self.getType()
        o = other.getType()
        if s == o:
            for c1,c2 in zip(self.cards,other.cards):
                if c1 != c2:
                    return CARDS[c1] < CARDS[c2]
        else:
            return s < o


def main():
    with open('input.txt') as f:
        lines = f.read().split('\n')

    hands = []
    for line in lines:
        cards, bid = line.split()
        hands.append(Hand(cards,bid))
    
    money = 0
    for i,hand in enumerate(sorted(hands)):
        money += hand.bid * (i + 1)
        
    
    print(money)
        

    


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}")
