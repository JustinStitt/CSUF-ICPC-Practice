# https://open.kattis.com/submissions/8404071
import sys
import math


def readin():
    kitten = input()
    path = dict()
    for line in sys.stdin:
        line = line.rstrip()
        line = line.split(' ')
        dest = line[0]
        if dest == '-1': break
        for src in range(1, len(line)):
            path[line[src]] = dest
    return kitten, path


def findPath(start, lookup):
    if lookup.get(start, None) == None: # at root
        return [start]
    dest = lookup[start]
    return [start] + findPath(dest, lookup)

def main():
    start, lookup = readin()
    path = findPath(start, lookup)
    print(*path)

main()

