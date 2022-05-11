#!/usr/bin/env python 
def fyi(n):
    if (str(n)[0:3] == "555"):
        return 1
    return 0

def main():
    print(fyi(int(input())))
    return

if __name__ == "__main__":
    main()