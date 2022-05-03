#!/usr/bin/env python 
def tarifa():
    x = int(input())
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))
    
    total = x
    for val in p:
        total += x - val
    return total

def main():
    print(tarifa())
    return

if __name__ == "__main__":
    main()