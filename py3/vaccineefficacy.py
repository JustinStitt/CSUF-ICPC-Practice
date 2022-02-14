n = int(input())

vax = list([0] * 3)
novax = list([0] * 3)

vax_count = 0
novax_count = 0

for _ in range(n):
	inp = [x for x in input()]
	group = inp[0]
	status = inp[1:]
	if group == 'Y': vax_count += 1
	else: novax_count += 1

	g = vax if group == 'Y' else novax

	for (i, v) in enumerate(status):
		g[i] += 1 if v == 'Y' else 0


vax_infected_rates = [x/vax_count for x in vax]
novax_infected_rates = [x/novax_count for x in novax]

# 0.6667, 0.5, .8

for i in range(3):
	if vax_infected_rates[i] >= novax_infected_rates[i]:
		print('Not Effective')
		continue
	perc = 1 - (vax_infected_rates[i]/novax_infected_rates[i])
	perc *= 100.0
	print(f'{perc:.6f}')


# vax = {A: 4, B: ?, C:?}