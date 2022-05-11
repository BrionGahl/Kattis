#!/usr/bin/env python 
def fillip(a, b):
    if int(a[::-1]) > int(b[::-1]):
        return a[::-1]
    return b[::-1]

def main():
    vals = input().split(" ")
    print(fillip(vals[0], vals[1]))
    return

if __name__ == "__main__":
    main()