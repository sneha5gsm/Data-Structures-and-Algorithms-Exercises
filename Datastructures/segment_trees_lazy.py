#!/bin/python3

import math
import os
import random
import re
import sys

#least = sys.minsize
least = -1
def updateRange(lazy, arr, tree, node, start, end , l, r, value):
    if lazy[node] != 0:
        tree[node] = tree[node] + lazy[node]
        if start != end:
            lazy[2*node + 1] = lazy[2*node + 1] + lazy[node]
            lazy[2*node + 2] = lazy[2*node + 2] + lazy[node]
        lazy[node] = 0
    if start> end or l>end or r< start:
        return
    if l <= start and end <= r:
        # print('inside eeee')
        tree[node] = tree[node] + value
        # print(tree)
        if end !=start:
            lazy[2*node + 1] = lazy[2*node + 1] + value
            lazy[2*node + 2] = lazy[2*node + 2] + value
        return
    mid = (start + end)//2
    updateRange(lazy, arr, tree, 2*node+1, start, mid, l, r, value)
    updateRange(lazy, arr, tree, 2*node+2, mid+1, end, l, r, value)
    # print('---------')
    # print(tree)
    tree[node] = max(tree[2*node+1], tree[2*node + 2])
    # print(tree)

def queryRange(lazy,arr, tree, node, start, end, l , r):
    if start>end or start>r or end< l:
        return 0;
    if lazy[node] !=0:
        tree[node] = tree[node] + lazy[node]
        if start != end:
            lazy[2*node + 1] = lazy[2*node + 1] + lazy[node]
            lazy[2*node + 2] = lazy[2*node + 2] + lazy[node]
        lazy[node] = 0
    if start >= l and end<=r:
        return tree[node]
    mid = (start + end)//2
    p1 = queryRange(lazy, arr, tree, 2*node+1, start, mid, l, r)
    p2 = queryRange(lazy, arr, tree, 2*node+2, mid +1, end, l, r)
    return max(p1, p2)

def arrayManipulation(n, m, queries):
    arr = [0] * n
    x = int(math.log(n, 2)) +2
    # print(str(x))
    x = int(math.pow(2,x) -1)
    # print(x)
    # print('==')
    tree = [0] *x
    lazy = [0]*x
    maximum  = -1
    for i in range(m):
        a = queries[i][0] - 1
        b = queries[i][1]
        print(queries[i])
        value = queries[i][2]
        updateRange(lazy, arr, tree, 0, 0, n-1, a, b-1, value)
        # print(tree)
        # for j in range(a, b):
        #     updateRange(arr, tree, 0, , n-1, j, value)
    # print(tree)
    # print(lazy)
    y=queryRange(lazy, arr, tree, 0, 0, n-1, 0, n-1)
    # print(y)
    return y


# if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
inputFile = open('inputFile', 'r')
nm = inputFile.readline().split()

n = int(nm[0])

m = int(nm[1])

queries = []

for _ in range(m):
    queries.append(list(map(int, inputFile.readline().rstrip().split())))
print(n)
print(m)
print(queries[0])
print('----')

result = arrayManipulation(n, m, queries)
print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
