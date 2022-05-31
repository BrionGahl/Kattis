#!/usr/bin/env python

def autori(names):
    initials = ""
    for name in names:
        initials += name[0]
    return initials

def main():
    names = input().split("-")
    print(autori(names))
    return

if __name__ == "__main__":
    main()