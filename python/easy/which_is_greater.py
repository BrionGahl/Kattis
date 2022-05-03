#!/usr/bin/env python 
def greater_than(num1, num2):
    return 1 if num1 > num2 else 0

def main():
    x = input()
    x = x.split(" ")
    print(greater_than(x[0], x[1]))
    return

if __name__ == "__main__":
    main()