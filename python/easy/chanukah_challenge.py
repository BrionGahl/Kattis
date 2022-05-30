#!/usr/bin/env python

def chanukah(dataset):
    for index, pair in enumerate(dataset):
        candles = 0
        for x in range(pair[1]):
            candles += (2 + x)
        yield tuple((index + 1, candles))
    return 

def main():
    p = int(input())
    data = []
    for i in range(p):
        data.append(tuple([int(x) for x in input().split(" ")]))
        
    for pair in chanukah(data):
        print(pair[0], pair[1])
    return

if __name__ == "__main__":
    main()