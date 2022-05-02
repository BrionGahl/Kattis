#!/usr/bin/env python 

def planina(num):
    val = 2
    for i in range(num):
        val += 2**i
    return val**2

def main():
    print(planina(int(input())))
    return

if __name__ == "__main__":
    main()