from math import sqrt
import sys


def isPrime(n: int):
    for x in range(2, int(sqrt(n))+1):
        if n % x == 0:
            return False
    return True


def solve(i: int, j: int, k, primes):
	total = 0
	for x in range(i-1, j):
		inquiry = str(primes[x])
		if k in inquiry:
			total += 1
	return total

def main():
	primes = []
	x = 1
	while 1:
		x += 1
		if isPrime(x):
			primes.append(x)
			if len(primes) == 100000:
				break
	for line in sys.stdin:
		(i, j) = [int(x) for x in line.split(' ')]
		k = input()
		res = solve(i, j, k, primes)
		print(res)

main()
