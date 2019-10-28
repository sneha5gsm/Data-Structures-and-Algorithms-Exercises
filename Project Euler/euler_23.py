t = int(raw_input())
abundants = {12: True}
done = {24: True}
for a0 in xrange(t):
    n = int(raw_input().strip())
    if n < 23:
        print 'NO'
    elif n == 24:
        print 'YES'
    elif n > 28123:
        print 'YES'
    else:
        if n in done.keys():
            print 'YES'
        else:
            i = n
            while i > 12:
                # print 'while'
                # print i
                if i in abundants.keys():
                    # print 'heree'
                    break
                else:
                    j = 2
                    sum = 1
                    while j < i:
                        if i % j == 0:
                            sum = sum + j
                        j = j + 1
                    # print sum
                    if sum > i:
                        abundants[i] = True
                i = i - 1
            flag = 0
            k = abundants.keys()
            for key in k:
                if (n - key) in k:
                    flag = 1
                    # print str(n-key)
                    print 'YES'
                    break
            if flag == 0:
                # print 'inisdeeee'
                print 'NO'
# print done
# print abundants


