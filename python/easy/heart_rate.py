#!/usr/bin/env python
def abpm(b, p):
    bpm = (60 * b) / p
    alteration = bpm / b
    print("%.4f %.4f %.4f" % (bpm - alteration, bpm, bpm + alteration))
    return 
def main():
    vals = []
    
    n = int(input())    
    for i in range(n):
        vals.append(input().split(" "))   

    for val in vals:
        abpm(int(val[0]), float(val[1]))
    return

if __name__ == "__main__":
    main()