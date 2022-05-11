#!/usr/bin/env python

def hissing(word):
    for index, letter in enumerate(word):
        if (letter == 's' and index != len(word) - 1 and word[index + 1] == 's'):
            return True
    return False

def main():
    word = input() 
    if (hissing(word)):
        print("hiss")
        return
    print("no hiss")     
    return

if __name__ == "__main__":
    main()