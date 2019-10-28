#!/bin/python

import math
import os
import random
import re
import sys


# Complete the twoPluses function below.
def callFn(grid1, i, j, n, m):
    grid = grid1[:]
    area1 = 1
    a = 1
    if (i + a) < n and (i - a) >= 0 and (j + a) < m and (j - a) >= 0:
        while grid[i + a][j] == 'G' and grid[i - a][j] == 'G' and grid[i][j + a] == 'G' and grid[i][j - a] == 'G':
            grid[i + a] = grid[i + a][:j] + 'U' + grid[i + a][j + 1:]
            grid[i - a] = grid[i - a][:j] + 'U' + grid[i - a][j + 1:]
            grid[i] = grid[i][:j + a] + 'U' + grid[i][j + a + 1:]
            grid[i] = grid[i][:j - a] + 'U' + grid[i][j - a + 1:]
            area1 = area1 + 4
            a = a + 1
            if (i + a) >= n or (i - a) < 0 or (j + a) >= m or (j - a) < 0:
                break
    maxproduct = 0
    while i < n:
        while j < m:
            if grid[i][j] == 'G':
                area2 = 1
                a = 1
                flag = 0
                if (i + a) < n and (i - a) >= 0 and (j + a) < m and (j - a) >= 0:
                    while grid[i + a][j] == 'G' and grid[i - a][j] == 'G' and grid[i][j + a] == 'G' and grid[i][
                        j - a] == 'G':
                        area2 = area2 + 4
                        a = a + 1
                        if (i + a) >= n or (i - a) < 0 or (j + a) >= m or (j - a) < 0:
                            flag = 1
                            break
                else:
                    flag = 1
                if flag == 0:
                    if (grid[i + a][j] == 'B' or grid[i - a][j] == 'B' or grid[i][j + a] == 'B' or grid[i][
                        j - a] == 'B') == 0:
                        area2 = 0
                if (area1 * area2) > maxproduct:
                    maxproduct = area1 * area2
            j = j + 1
        j = 0
        i = i + 1
    return maxproduct


def twoPluses(grid, n, m):
    i = 0
    maxarea = 0
    while i < n:
        j = 0
        while j < m:
            if grid[i][j] == 'G':
                area = callFn(grid, i, j, n, m)
                if area > maxarea:
                    maxarea = area
            j = j + 1
        i = i + 1
    return maxarea


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    grid = []

    for _ in xrange(n):
        grid_item = raw_input()
        grid.append(grid_item)
    result = twoPluses(grid, n, m)

    fptr.write(str(result) + '\n')

    fptr.close()




12 12
GGGGGGGGGGGG
GBGGBBBBBBBG
GBGGBBBBBBBG
GGGGGGGGGGGG
GGGGGGGGGGGG
GGGGGGGGGGGG
GGGGGGGGGGGG
GBGGBBBBBBBG
GBGGBBBBBBBG
GBGGBBBBBBBG
GGGGGGGGGGGG
GBGGBBBBBBBG


81