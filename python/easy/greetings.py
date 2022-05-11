#!/usr/bin/env python 
def greetings(string):
    return "h" + string[1:-1] * 2 + "y"

def main():
    string = input()
    print(greetings(string))
    return    

if __name__ == "__main__":
    main()