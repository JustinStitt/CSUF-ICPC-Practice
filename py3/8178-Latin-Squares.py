# https://icpcarchive.ecs.baylor.edu/external/81/8178.pdf
# submission #2687547
# verdict: Accepted
# Runtime: 0.036
# 2022-02-06
import sys
import math

A = []

def readin():
    while True:
        try:
            c = []
            n = int(input()) # num of rows
        except EOFError:
            return
        for i in range(n):
            b = []
            row = input()
            for col in row:
                b.append(int(col, n))
            c.append(b)
        A.append(c)

def isLatinSquare(m):
    # if count in row > 1 or count in col > 1 not Latin
    n = len(m)
    for i in range(n):
        for j in range(n):
            if m[i].count(m[i][j]) > 1: return False
            for ip in range(i+1, n):
                if m[ip][j] == m[i][j]: return False
    return True

def isReducedLatinSquare(m):
    # is first row in natural order
    # is first col in natural order
    n = len(m)
    if sorted(m[0]) != m[0]:
        return False
    fcol = []
    for r in range(n):
        fcol.append(m[r][0])
    if sorted(fcol) != fcol:
        return False
    return True

def main():
    readin()
    #print(A)
    for matrix in A:
        latin = isLatinSquare(matrix)
        reduced = latin and isReducedLatinSquare(matrix)
        # fizzbuzz lol
        if reduced:
            print('Reduced')
        elif latin:
            print('Not Reduced')
        else:
            print('No')
main()

