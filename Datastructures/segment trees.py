#!/bin/python3

import math
import os
import random
import re
import sys

#least = sys.minsize
least = -1

def update(arr, tree, node, start, end, idx, value):
    # print('--------- call')
    # print('start: ' + str(start))
    # print('end: ' + str(end))
    # print('idx: ' + str(idx))
    if start == end:
        print('node her: '+str(node))
        tree[node] = tree[node] + value
        arr[idx] = arr[idx] + value
    else:
        mid = (start + end)//2
        if start <= idx and idx <= mid:
            update(arr, tree, 2*node+1, start, mid, idx, value)
        else:
            update(arr, tree, 2*node + 2, mid +1, end, idx, value)
        print('node: '+ str(node))
        tree[node] = max(tree[2*node + 1] , tree[2*node + 2])

def query(node, start, end, l, r):
    if r<start or l>end:
        return minsize
    if l<=start and r>= end:
        return tree[node]
    mid = (start + end)/2
    p1 = query(2*node + 1, start, mid, l, r)
    p2 = query(2*node + 2, mid + 1, end, l, r)
    return max(p1, p2)




# def build(node, start, end):
#     if start == end:
#         tree[node] =
# Complete the arrayManipulation function below.
def arrayManipulation(n, m, queries):
    arr = [0] * n
    x = int(math.log(n, 2)) +2
    # print(str(x))
    x = int(math.pow(2,x) -1)
    # print(x)
    # print('==')
    tree = [0] *x
    maximum  = -1
    for i in range(m):
        a = queries[i][0] - 1
        b = queries[i][1]
        value = queries[i][2]
        for j in range(a, b):
            update(arr, tree, 0, 0, n-1, j, value)
    return tree[0]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, m, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
