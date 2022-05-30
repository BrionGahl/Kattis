#!/usr/bin/env python

def negative(temps):
    count = 0
    for temp in temps:
        if temp < 0:
            count += 1
    return count

def main():
    n = int(input())
    temps = [int(x) for x in input().split(" ")]
    print(negative(temps))
    return

if __name__ == "__main__":
    main()