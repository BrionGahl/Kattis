#!/usr/bin/env python

def combinations(num1, num2, num3):
    return num1 * num2 * num3
        
def main():
    x = input().split(" ")
    print(combinations(int(x[0]), int(x[1]), int(x[2])))
    return    

if __name__ == "__main__":
    main()