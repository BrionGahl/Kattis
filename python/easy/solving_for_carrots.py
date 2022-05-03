#!/usr/bin/env python 
def carrots():
    vals = input().split(" ")
    for i in range(int(vals[0])):
        input()
    return vals[1]

def main():
    print(carrots())
    return

if __name__ == "__main__":
    main()