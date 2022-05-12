#!/usr/bin/env python
 
def eye(string):
    if (len(string) % 2 != 0):
        return False
    
    return (ord(string[int(len(string)/2) - 1]) == ord(string[int(len(string)/2)]) - 1)

def main():
    if (eye(input())):
        print("correct")
        return
    print("fix")
    return

if __name__ == "__main__":
    main()