#!/usr/bin/evn python

def bijele(found):
    pieces = [1, 1, 2, 2, 2, 8]
    needed = ""
    
    for i, (piece, have) in enumerate(zip(pieces, found)):
        needed += str(piece - have) + " "
    
    return needed.strip()

def main():
    print(bijele([int(x) for x in input().split(" ")]))
    return

if __name__ == "__main__":
    main()