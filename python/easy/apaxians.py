#!/usr/bin/env python

def apaxians(s):
    out = " "
    for letter in s:
        if letter != out[-1]:
            out += letter
    return out.strip()

def main():
    print(apaxians(input()))
    return

if __name__ == "__main__":
    main()
    