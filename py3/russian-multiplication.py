import sys

def solve(c1: int, c2: int):
    c3 = c2 if c1 & 1 else 0
    while(c1 >= 1):
        print(c1, c2, c3)
        c1 //= 2
        c2 *= 2
        if int(c1) & 1:
            c3 += c2
    return c3


for line in sys.stdin:
    c1, c2 = [int(x) for x in line.split(' ')]
    res = solve(c1, c2)
    print('=', res)



