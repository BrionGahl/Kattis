#!/usr/bin/env python 
def quadrant(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    return 4

def main():
    x = int(input())
    y = int(input())
    print(quadrant(x, y))
    return    

if __name__ == "__main__":
    main()