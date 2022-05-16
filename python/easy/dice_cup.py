#!/usr/bin/env python

def dice_cup(n, m):
    if n > m:
        for i in range(m, n + 1):
            yield i + 1
    else:
        for i in range(n, m + 1):
            yield i + 1

def main():
    dice = [int(x) for x in input().split(" ")]
    for val in dice_cup(dice[0], dice[1]):
        print(val)
    return

if __name__ == "__main__":
    main()