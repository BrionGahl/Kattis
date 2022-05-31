#!/usr/bin/env python

DOMINANT = {'A': 11, 'K': 4, 'Q': 3, 'J': 20, 'T': 10, '9': 14, '8': 0, '7': 0}
NONDOMINANT = {'A': 11, 'K': 4, 'Q': 3, 'J': 2, 'T': 10, '9': 0, '8': 0, '7': 0}

def bela(suit, cards):
    count = 0
    for card in cards:
        count = count + DOMINANT[card[0]] if card[1] == suit else count + NONDOMINANT[card[0]]
    return count

def main():
    nb = input().split(" ")
    cards = []
    
    for i in range(4 * int(nb[0])):
        cards.append(input())
    
    print(bela(nb[1], cards))
    return

if __name__ == "__main__":
    main()