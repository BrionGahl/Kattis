#!/usr/bin/env python

def count(s):
    count = 0
    for letter in s:
        if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    return count

def main():
    print(count(input()))
    return

if __name__ == "__main__":
    main()