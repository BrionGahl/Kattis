#!/usr/bin/env python
 
import math

def faktor():
    input_values = input()
    vals = input_values.split(" ")
    
    out = math.ceil(int(vals[0]) * (int(vals[1]) - 0.99))
    return out
    
    
def main():
    print(faktor())
    return    

if __name__ == "__main__":
    main()