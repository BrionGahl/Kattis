#!/usr/bin/env python       
def main():
    total = 1
    
    n = int(input())
    for i in range(n):
        total += int(input()) - 1 
    print(total)
    return    

if __name__ == "__main__":
    main()