
def recfn(z, alpha, i, alls):
    x = len(z) - 1
    flag = 0
    while flag == 0 and i < x:
        # print 'inisde while loop'
        if alpha[z[i]] == -1:
            # print 'insde if'
            # print alpha
            alpha[z[i]] = i
            # print alpha
            i = i + 1
        else:
            # print '=----'
            flag = 1
            # print 'inside else'
            # a=alpha[z[i]]
            a = z.find(z[i])
            x = z[:a] + z[a + 1:]
            y = z[:i] + z[i + 1:]
            alphatemp = alpha.copy()

            alphatemp[z[i]] = i - 1
            # print y
            # print alpha
            # print i
            # print x
            # print alphatemp
            recfn(y, alpha, i, alls)
            recfn(x, alphatemp, i, alls)
    if i >= x:
        # print 'inside append'
        try:
            x = alls2[z]
        except:
            alls2[z] = 0
            alls.append(z)
            # print alls
        return


# Write your code here
t = 1
while t == 1:
    try:
        alls = []
        alls2 = {}
        alpha = {'a': -1, 'b': -1, 'c': -1, 'd': -1, 'e': -1, 'f': -1, 'g': -1, 'h': -1, 'i': -1, 'j': -1, 'k': -1,
                 'l': -1, 'm': -1, 'n': -1, 'o': -1, 'p': -1, 'q': -1, 'r': -1, 's': -1, 't': -1, 'u': -1, 'v': -1,
                 'w': -1, 'x': -1, 'y': -1, 'z': -1}
        z = raw_input().strip()
        s =len(z)
        i=1
        p=z[0]+''
        while i<s:
            if z[i] != z[i-1]:
                p=p+z[i]
            i=i+1
        print p
        p = p + '1'
        # s = len(p)
        i = 0
        recfn(p, alpha, 0, alls)
        # print '==='
        # print alls
        alls.sort()
        y = alls[0]
        y = y[:-1]
        print y
    except:
        t = 0
