#!/usr/bin/env python 
def pot():
    operands = []
    
    n = int(input())
    for i in range(n):
        operands.append(input())
    
    solution = 0
    for operand in operands:
        solution += int(operand[0:-1])**int(operand[-1])
    
    return solution

def main():
    print(pot())
    return    

if __name__ == "__main__":
    main()