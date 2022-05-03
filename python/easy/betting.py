#!/usr/bin/env python 
def betting():
    opt_one = int(input())
    opt_two = 100 - opt_one
    
    payout_ratio_one = 1 / (opt_one / 100)
    payout_ratio_two = 1 / (opt_two / 100)
    
    print("%.10f" % payout_ratio_one)
    print("%.10f" % payout_ratio_two)
    
    return

def main():
    betting()
    return    

if __name__ == "__main__":
    main()