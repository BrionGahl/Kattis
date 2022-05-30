#!/usr/bin/env python

def double_pass(pwd1, pwd2):
    diff = 0
    for tup in zip(pwd1, pwd2):
        if tup[0] != tup[1]:
            diff += 1
    return 2**diff

def main():
    pwd1 = input()
    pwd2 = input()
    
    print(double_pass(pwd1, pwd2))
    
    return

if __name__ == "__main__":
    main()