import sys
import math


def solve(time):
    print(time)
    for d in [8,4,2,1]:
        s = 0
        for c in time:
            s += 1
            print('*' if d&int(c) else '.', end='') 
            print(' ' if s != 4 else '', end ='')
            if s == 2: print('  ', end = '')
        print()

for line in sys.stdin:
    line = line.rstrip()
    solve(line)