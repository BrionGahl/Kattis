#!/usr/bin/env python
 
def decode(string):
    n = int(len(string) ** (1/2))

    matrix = []
    for i in range(0, len(string), n):
        matrix.append(string[i:i + n])
    decoded = ""
    for row in rotate(matrix, n):
        decoded += row
    return decoded

def rotate(matrix, n):
    rotated_matrix = []
    for i in range(n):
        rotated_matrix.append("")
    
    for row in matrix:
        for i in range(n):
            rotated_matrix[n - 1 - i] += row[i] 
    
    return rotated_matrix

def main():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    
    for word in words:
        print(decode(word))
    
    return

if __name__ == "__main__":
    main()