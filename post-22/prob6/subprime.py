from math import sqrt
import sys

def sieve(max = 2**21):
    primes = [True for x in range(max)]
    i = 1
    while i*i <= len(primes):
        i += 1
        if not primes[i]: continue
        for j in range(i**2, len(primes), i):
            primes[j] = False
        
    return [x for x in range(len(primes)) if primes[x] == True][2:100002]

def solve(i, j, k, primes):
    total = 0
    for x in primes[i-1:j]:
        if k in str(x): total += 1
    return total

primes = sieve()

for line in sys.stdin:
    (i, j) = [int(x) for x in line.split(' ')]
    k = input()


    res = solve(i, j, k, primes)
    print(res)