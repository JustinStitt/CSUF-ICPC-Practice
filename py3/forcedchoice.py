n, p, s = [int(x) for x in input().split()]

master = set([x for x in range(1, n+1)])
# {0 , 1, 2, 3, ..., n-1, n}

for x in range(s):
	sel = set([int(x) for x in input().split()][1:])
	if p in sel:
		master = sel
		print('KEEP')
		continue
	for x in sel:
		master.remove(x)
	print('REMOVE')


