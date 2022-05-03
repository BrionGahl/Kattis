#!/usr/bin/env python 
def area_triangle(height, base):
    return (1/2) * base * height

def main():
    x = input()
    x = x.split(" ")
    print(area_triangle(int(x[0]), int(x[1])))
    return

if __name__ == "__main__":
    main()