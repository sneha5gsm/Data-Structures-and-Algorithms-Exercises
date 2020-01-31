######################## Question ################
# Supervin loves to eat candies. Today, his favorite candy shop is offering N candies, which are arranged in a line. The i-th candy in the line (counting starting from 1) has a sweetness level Si. Note that the sweetness level of a candy might be negative, which means the candy tastes bitter.

# Supervin likes to eat sweet candies. However, candies with a combined sweetness level of more than D would be too much sweetness even for him. Supervin also realises that a candy with an odd sweetness level is "odd", and he does not want to eat more than O odd candies. In other words, an odd candy is a candy with a sweetness level that is not evenly divisible by 2. Additionally, since Supervin is in a rush, he can only eat a single contiguous subset of candies.

# Therefore, he wants to eat a contiguous non-empty subset of candies in which there are at most O odd candies and the total sweetness level is maximized, but not more than D. Help Supervin to determine the maximum total sweetness level he can get, or return IMPOSSIBLE if there is no contiguous subset satisfying these constraints.

# Input
# The first line of the input gives the number of test cases, T. T test cases follow. Each test case contains two lines. The first line contains three integers N, O, and D, as described above. The second line contains seven integers X1, X2, A, B, C, M, L; these values are used to generate the values Si, as follows:

# We define:

# Xi = (A × Xi - 1 + B × Xi - 2 + C) modulo M, for i = 3 to N.
# Si = Xi + L, for i = 1 to N.
# Output
# For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the maximum total sweetness level Supervin can get, or IMPOSSIBLE if there is no possible contiguous subset satisfying the problem constraints.

# Limits
# 1 ≤ T ≤ 100.
# 2 ≤ N ≤ 5 × 105.
# 0 ≤ O ≤ N.
# -1015 ≤ D ≤ 1015.
# 0 ≤ X1, X2, A, B, C ≤ 109.
# 1 ≤ M ≤ 109.
# Small dataset
# L = 0.
# Large dataset
# -5 × 108 ≤ L ≤ 0.
# Sample

# Input 
 	
# Output 
 
# 5
# 6 1 1000000000000000
# 1 1 1 1 0 100 0
# 6 1 -100
# 1 1 1 1 0 100 0
# 10 1 8
# 4 3 4 1 5 20 -10
# 10 2 8
# 4 3 4 1 5 20 -10
# 10 1 8
# 4 3 4 1 5 20 -19

# Case #1: 13
# Case #2: IMPOSSIBLE
# Case #3: 7
# Case #4: 8
# Case #5: -5

# Note that the last three sample cases would not appear in the Small dataset.

# In Sample Case #1, the generated array of sweetness values Si is: [1, 1, 2, 3, 5, 8], where the bold and underlined numbers are the odd numbers. Since Supervin can only eat one odd candy, he can get a maximum total sweetness level by taking the fifth and the sixth candies.

# In Sample Case #2, the generated array of sweetness values Si is the same as in Sample Case #1. However, this time Supervin cannot eat candies with a total sweetness level of more than -100, so no contiguous subset of candies satisfies the constraints.

# In Sample Case #3, the generated array of sweetness values Si is: [-6, -7, -9, 2, 4, 3, 1, -8, -6, -7], where the bold and underlined numbers are the odd numbers. Since Supervin can only eat one odd candy and he cannot eat candies with a total sweetness level of more than 8, he can get the maximum total sweetness level by taking the fifth and the sixth candies.

# In Sample Case #4, the generated array of sweetness values Si is the same as in Sample Case #3. However, this time Supervin can eat two odd candies. Therefore, he can get a maximum total sweetness level by taking the fifth, the sixth, and the seventh candies.

# In Sample Case #5, the generated array of sweetness values Si is: [-15, -16, -18, -7, -5, -6, -8, -17, -15, -16] where the bold and underlined numbers are the odd numbers. Note that it is possible for the maximum total sweetness level to be negative.

# Note: We do not recommend using interpreted/slower languages for the Large dataset of this problem.


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
