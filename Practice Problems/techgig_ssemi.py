''' Read input from STDIN. Print your output to STDOUT '''
# Use input() to read input from STDIN and use print to write your output to STDOUT
groups = []
keyDict = {}


def dfs(a):
    numberOfVertices = len(a)
    v = [0] * (numberOfVertices)
    i = 1
    g = 0
    while i < numberOfVertices:
        if v[i] == 0:
            p = dfsVisit(i, a, v, [i], g)
            groups.append(p)
            g = g + 1
        i = i + 1


def dfsVisit(b, a, v, path, g):
    keyDict[b] = g
    v[b] = 1
    for x in a[b]:
        if v[x] == 0:
            path.append(x)
            dfsVisit(x, a, v, path, g)
    return path


def getLongest(symphony):
    i = 0
    z = len(symphony)
    length = 0
    if z % 2 == 0:
        limit = z / 2 - 1
    else:
        limit = z / 2
    while i <= limit:
        print '-------'
        print i
        print z-1-i
        if symphony[i] == symphony[z - 1 - i]:
            if i == (z - i - 1):
                print 'inside first if'
                print symphony
                print length
                length = length + 1
            else:
                print 'inside seconf if'
                print symphony
                print length
                length = length + 2
        elif symphony[z - 1 - i] in groups[keyDict[symphony[i]]]:
            print 'inside elif'
            print symphony
            print length
            length = length + 2
        else:
            print 'inisde else'
            print symphony
            print length
            print symphony[i:(z-1-i)]
            print symphony[i+1:(z-i)]
            length = length + max(getLongest(symphony[i:(z - 1 - i)]), getLongest(symphony[i + 1:(z - i)]))
            break
        i = i + 1
    return length


def main():
    n = int(raw_input().strip())
    pairsDict = [0] * (n + 1)
    i = 1
    while i <= n:
        pairsDict[i] = []
        i = i + 1
    # print pairsDict
    m = int(raw_input().strip())
    r = int(raw_input().strip())
    i = 0
    while i < m:
        var1, var2 = [int(x) for x in raw_input().split()]
        pairsDict[var1].append(var2)
        pairsDict[var2].append(var1)
        i = i + 1
    dfs(pairsDict)
    print pairsDict
    print groups
    print keyDict
    z = int(raw_input().strip())
    i = 0
    symphony = []
    while i < z:
        symphony.append(int(raw_input().strip()))
        i = i + 1
    # print symphony
    ans = getLongest(symphony)
    print ans


main()

