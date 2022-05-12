#!/usr/bin/env python
 
def electric(n, chain):
    appliances = 0
    for count in chain:
        appliances += count
    return appliances - (n - 1)
def main():
    n = int(input())
    chains = []
    for i in range(n):
        chains.append([int(val) for val in input().split(" ")])
    for chain in chains:
        print(electric(chain[0], chain[1:]))
    return

if __name__ == "__main__":
    main()