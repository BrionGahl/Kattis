#!/usr/bin/env python

# r = revenue if you do not advertise
# e = expected revenue if you do advertise
# c = cost of advertising
def nasty_hacks(r, e, c):
    cost_eff = e - c
    if (cost_eff < r):
        return "do not advertise"
    elif(cost_eff > r):
        return "advertise"
    return "does not matter"
       
def main():
    lines = []
    n = int(input())
    for i in range(n):
        lines.append(input().split(" "))
    for line in lines:
        print(nasty_hacks(int(line[0]), int(line[1]), int(line[2])))
    return    

if __name__ == "__main__":
    main()