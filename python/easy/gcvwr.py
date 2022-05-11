#!/usr/bin/env python 
def gcvwr(g, t, items):
    capacity = g - t
    load_weight = 0
    for item in items:
        load_weight += item 
    return int((capacity * .9) - load_weight)

def main():
    vals = [int(val) for val in input().split(" ")] # input: g t n
    g = vals[0]
    t = vals[1]
    n = vals[2]
        
    items = [int(item) for item in input().split(" ")]
    if len(items) == n:
        print(gcvwr(g, t, items))
    return    

if __name__ == "__main__":
    main()