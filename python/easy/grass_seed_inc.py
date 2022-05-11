#!/usr/bin/env python 
def sow_cost(cost, lawns):
    total = 0.0
    for lawn in lawns:
        total += (float(lawn[0]) * float(lawn[1]) * cost)
    return total

def main():
    c = float(input()) # cost
    l = int(input()) # number of lawns
    lawns = []
    for i in range(l):
        lawns.append(input().split(" "))
    print("%.7f" % sow_cost(c, lawns))
    return    

if __name__ == "__main__":
    main()