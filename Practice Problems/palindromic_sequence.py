inputFile = open('inputFile', 'r')
outputFile = open('outputFile', 'w+')
testCases = int(inputFile.readline())

def recursiveFn( all2,t,all,l,n, s, k):
    alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    i=0
    # if len(all)<=total:
    if len(s)<n:
        # print 'inside'
        while i <l:
            # print 'in'
            x=s+alpha[i]
            if x == x[::-1]:
                all=all+'.'
                all2.append(x)
            if len(all) == k:
                print all2
                print '-----'
                print all
                # print x
                fileLine = 'Case #' + str(t + 1) + ": " + str(len(x)) + '\n'
                outputFile.write(fileLine)
                return len(x)
            else:
                recursiveFn(all2,t,all,l,n,x, k)
            i=i+1

for t in range(0, testCases):
    z = inputFile.readline()
    if z[len(z) - 1] == '\n':
        z = z[: len(z) - 1]
    line = map(int, z.split(' '))
    l = line[0]
    n = line[1]
    k = line[2]
    total =0
    # total = recursiveFn(l,n)
    x=n/2
    y=n
    while y>0:
        x=y/2
        if y%2==0:
            total = total +pow(l, x)
        else:
            total =total + pow(l, x)*l
        y=y-1
    # print total
    ans = 0
    if k>total:
        fileLine = 'Case #' + str(t + 1) + ": " + str(0) + '\n'
        outputFile.write(fileLine)
    else:
        g = recursiveFn([],t,'', l, n, '', k)

