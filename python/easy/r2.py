#!/usr/bin/env python 
def r2(r1, s):
    return 2 * s - r1

def main():
    vals = input().split(" ")
    print(r2(int(vals[0]), int(vals[1])))
    return

if __name__ == "__main__":
    main()