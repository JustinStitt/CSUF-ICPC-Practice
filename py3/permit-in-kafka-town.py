clerks = [int(input()) for i in range(int(input()))]

print(sum([1 for i in range(len(clerks)- 1) if clerks[i] > clerks[i+1]]) + 1)