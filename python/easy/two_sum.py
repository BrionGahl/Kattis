#!/usr/bin/env python 
def sum(num1, num2):
    return num1 + num2

def main():
    x = input()
    x = x.split(" ")
    print(sum(int(x[0]), int(x[1])))
    return

if __name__ == "__main__":
    main()