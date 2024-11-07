#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kingdomDivision' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY roads
#

MOD = 10 ** 9 + 7


def kingdomDivision(n, roads):
    from collections import defaultdict

    sys.setrecursionlimit(200000)

    graph = defaultdict(list)
    for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)

    memo_f = {}
    memo_g = {}

    # f(node, parent)
    def f(node, parent):
        if (node, parent) in memo_f:
            return memo_f[(node, parent)]
        res = 1
        for child in graph[node]:
            if child == parent:
                continue
            res = res * (2 * f(child, node) + g(child, node)) % MOD
        res = (res - g(node, parent) + MOD) % MOD
        memo_f[(node, parent)] = res
        return res

    # g(node, parent)
    def g(node, parent):
        if (node, parent) in memo_g:
            return memo_g[(node, parent)]
        res = 1
        for child in graph[node]:
            if child == parent:
                continue
            res = res * f(child, node) % MOD
        memo_g[(node, parent)] = res
        return res

    return 2 * f(1, 0) % MOD


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    roads = []

    for _ in range(n - 1):
        roads.append(list(map(int, input().rstrip().split())))

    result = kingdomDivision(n, roads)

    fptr.write(str(result) + '\n')

    fptr.close()
