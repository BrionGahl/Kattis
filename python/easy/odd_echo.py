#!/usr/bin/env python

def odd_echo(words):
    for index, word in enumerate(words):
        if (index % 2 == 0): 
            yield(word)        
def main():
    words = []
    
    n = int(input())
    for i in range(n):
        words.append(input())
        
    for value in odd_echo(words):
        print(value)
    return    

if __name__ == "__main__":
    main()