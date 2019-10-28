inputFile = open('inputFile', 'r')
outputFile = open('outputFile', 'w+')
testCases = int(inputFile.readline())
for t in range(0, testCases):
    z = inputFile.readline()
    if z[len(z) - 1] == '\n':
        z = z[: len(z) - 1]
    line = map(int, z.split(' '))
    n = line[0]
    o=line[1]
    d = line[2]
    z = inputFile.readline()
    if z[len(z) - 1] == '\n':
        z = z[: len(z) - 1]
    line = map(int, z.split(' '))
    x1 = line[0]
    x2 = line[1]
    a = line[2]
    b=line[3]
    c = line[4]
    m=line[5]
    l=line[6]
    sweetArray = [0]*n
    sweetArray[0] = x1 + l
    sweetArray[1] = x2 + l
    # odd =0
    # if (x1+1)%2 != 0:
    #     odd = odd +1
    # sweetArray[0]=(x1+l, odd)
    # if (x2+1)%2 !=0:
    #     odd =odd+1
    # sweetArray[1] = (sweetArray[0][0] + x2+l, odd)
    i=2
    x = 0
    s=0
    while i<n:
        # print 'x1'
        # print x1
        # print 'x2'
        # print x2
        x = (a*x2 + b*x1 +c)%m
        sweetArray[i]= x+l
        x1 = x2
        x2 = x
        i=i+1
    # while i<n:
    #     # print 'x1'
    #     # print x1
    #     # print 'x2'
    #     # print x2
    #     x = (a*x2 + b*x1 +c)%m
    #     if x%2!=0:
    #         odd =odd+1
    #     sweetArray[i]= (sweetArray[i-1][0] + x+l, odd)
    #     x1 = x2
    #     x2 = x
    #     i=i+1
    # print 'sweetarray'
    # print sweetArray
    i=0
    j=0
    odd = 0
    sweet='IMPOSSIBLE'
    # maxSweet = 'IMPOSSIBLE'
    # while i<n:
    #     j=i+1
    #     while j<n:
    #         if sweetArray[j][0] - sweetArray[i][0] <=d and sweetArray[j][1] - sweetArray[i][1] <=o and (maxSweet=='IMPOSSIBLE' or sweetArray[j][0] - sweetArray[i][0]>maxSweet):
    #             maxSweet = sweetArray[j][0] - sweetArray[i][0]
    #         j=j+1
    #     i=i+1
    flag = 0
    flag3=0
    odd2=0
    while j<n:
        odd2 = odd
        if sweetArray[j]%2 == 1:
            odd2 = odd +1
        # print 'sweet j ' + str(sweetArray[j])
        # print sweet
        # print odd
        previousI = -1
        if sweet =='IMPOSSIBLE':
            s = sweetArray[j]
        else:
            if sweet <0:
                s = sweetArray[j]
                previousI = i
                i=j
                odd2=0
                if sweetArray[j] % 2 == 1:
                    odd2 = 1
            else:
                s = sweet + sweetArray[j]
        # print 'odd2 ' + str(odd2) + ' s1 ' + str(s)
        if s>d or odd2>o:
            flag2=0
            s1 = s
            while flag2==0:
                if i>j:
                    s1='IMPOSSIBLE'
                    break
                # print 'inside if2'
                s1 = s1 - sweetArray[i]
                # print 's1 '+ str(s1) + ' i '+ str(i)
                if sweetArray[i]%2 ==1:
                    odd2=odd2-1
                if s1<=d and odd2 <=o:
                    # print 'if3'
                    flag2=1
                i = i + 1
                # print 'odd2 ' + str(odd2) + ' s1 ' + str(s1) + ' i '+str(i)

            if s1 != 'IMPOSSIBLE':
                if sweet != 'IMPOSSIBLE':
                    if s1>sweet and s1<=d and odd2<=o:
                        # flag3 = 1
                        sweet = s1
                        odd = odd2
                else:
                    sweet = s1
                    odd = odd2
            else:
                i = previousI
            j=j+1
            continue
        if sweet!='IMPOSSIBLE':
            if s>sweet:
                # print 'insideeeeeeeeeeeeeeee'
                # print 'swwert '+ str(sweet)
                # print 's '+str(s)
                # flag3=1
                sweet = s
                odd =odd2
            else:
                i = previousI
        else:
            sweet = s
            odd = odd2
        j=j+1
    print "###############    " + str(t+1)
    outputFile.write('Case #' + str(t + 1) + ": " + str(sweet) + '\n')
inputFile.close()
outputFile.close()
