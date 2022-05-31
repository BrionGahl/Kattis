#!/usr/bin/env python

def batter(n, data):
    total = 0
    walks = 0
    for val in data:
        if val == -1:
            walks += 1
            continue
        total += val
    return total / (n - walks)

def main():
    n = int(input())
    data = [int(x) for x in input().split(" ")]
    
    print(batter(n, data))
    return

if __name__ == "__main__":
    main()