#!/usr/bin/env python 
def qaly():
    n = int(input())
    qalyTotal = 0
    for i in range(n):
        vals = input().split(" ")
        qalyTotal += float(vals[0]) * float(vals[1])
    return qalyTotal

def main():
    print("%.3f" % qaly())
    return

if __name__ == "__main__":
    main()