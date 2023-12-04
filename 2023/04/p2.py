import time

def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()
    sum = 0
    cards = dict()
    for line in lines:
        card,info = line.split(':')
        _,card = card.strip().split()
        card = int(card)
        
        part1,part2 = info.split('|')
        winners = set(part1.strip().split())
        numbers = set(part2.strip().split())
   

        numberOfCard = cards.get(card,0) + 1
        cards[card] = numberOfCard
        
        numberOfWinners = len(numbers.intersection(winners))

        for i in range(card +1, card + numberOfWinners +1):
            if i in cards:
                cards[i] += numberOfCard
            else:
                cards[i] = numberOfCard

    for st in cards.values():
        sum += st
    print(sum)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time is : {end - start}")
