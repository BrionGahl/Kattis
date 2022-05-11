#!/usr/bin/env python 
def finding_a(string):
    for index, letter in enumerate(string):
        if (letter == 'a'):
            return string[index:]
    return 

def main():
    print(finding_a(input()))
    return

if __name__ == "__main__":
    main()