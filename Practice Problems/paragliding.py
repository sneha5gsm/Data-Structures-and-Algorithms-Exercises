####################### Question ###################################
# In order to advance in his quest to defeat the villainous Graphendorf, our hero Edge has to overcome a challenge in a shrine. The shrine is two-dimensional in the xy-plane, and there are N towers (of varying heights) erected along the x-axis of the plane. Each tower can be represented by a vertical line segment in a 2D plane. For tower i, the base of the tower is at (pi, 0), and the top of the tower is at (pi, hi). There are also K balloons floating in the plane. Each balloon can be represented by a single point in the 2D plane, with balloon i at position (xi, yi). Edge has to collect as many balloons as possible in this challenge.

# Fortunately, Edge has a trusty paraglider which he found in a different room of this shrine. He may choose to climb any tower and glide down from any position on the tower towards either the positive or negative direction of the x-axis. When he glides, he descends in a straight path that makes a 45 degrees angle relative to the tower. Edge can collect any balloons in his way when he glides down from the tower. He can repeat this process of climbing up a tower and jumping off any number of times. If he touches a tower during his descent, then he is considered to be on the tower at the point and climbing. You may assume Edge to be a single point in the xy-plane.

# Using a pair of goggles made from ancient technology, Edge was able to figure out the height and position of each tower and balloon. With this information, can you help Edge deduce the maximum number of balloons that he can collect in this shrine?

# Input
# The first line of the input gives the number of test cases, T. T test cases follow. Each test case contains five lines. The first line contains the integers N and K as described above. Each of the next four lines describe a recurrence used to generate the positions and heights of the towers and the x and y coordinates of the balloons. The four lines will each contain six integers in the following format:

# p1 p2 A1 B1 C1 M1
# h1 h2 A2 B2 C2 M2
# x1 x2 A3 B3 C3 M3
# y1 y2 A4 B4 C4 M4
# To generate the values for pi (from 3 to N), hi (from 3 to N), xi (from 3 to K) and yi (from 3 to K), we use the following recurrences:
# pi = (A1 × pi - 1 + B1 × pi - 2 + C1) modulo M1 + 1, for i = 3 to N.
# hi = (A2 × hi - 1 + B2 × hi - 2 + C2) modulo M2 + 1, for i = 3 to N.
# xi = (A3 × xi - 1 + B3 × xi - 2 + C3) modulo M3 + 1, for i = 3 to K.
# yi = (A4 × yi - 1 + B4 × yi - 2 + C4) modulo M4 + 1, for i = 3 to K.
# It is guaranteed that no two towers share the same position. However, it is possible for a tower to overlap with a balloon. In this case, we assume that the balloon can be collected. Note that two or more balloons might share a point; in that case, Edge can collect all of those balloons at once by passing through that point.
# Output
# For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the maximum number of balloons that Edge can collect.

# Limits
# 1 ≤ T ≤ 100.
# 0 ≤ Ai ≤ 109 for i = 1 to 4.
# 0 ≤ Bi ≤ 109 for i = 1 to 4.
# 0 ≤ Ci ≤ 109 for i = 1 to 4.
# 1 ≤ Mi ≤ 109 for i = 1 to 4.
# 1 ≤ p1, p2 ≤ 109.
# 1 ≤ h1, h2 ≤ 109.
# 1 ≤ x1, x2 ≤ 109.
# 1 ≤ y1, y2 ≤ 109.
# pi ≠ pj for i, j = 1 to N, i ≠ j.

# Small dataset
# 2 ≤ N ≤ 1000.
# 2 ≤ K ≤ 1000.
# Large dataset
# 2 ≤ N ≤ 105.
# 2 ≤ K ≤ 105.
# Sample

# Input 
 	
# Output 
 
# 2
# 3 2
# 1 4 1 1 0 11
# 4 1 1 1 8 11
# 2 5 0 0 0 11
# 4 1 0 0 0 11
# 5 5
# 2 4 1 0 1 13
# 4 4 0 1 12 13
# 1 4 1 1 0 13
# 3 5 1 1 7 13

# Case #1: 1
# Case #2: 4

# Note that the input for Sample Case #1 produces the scenario depicted in the problem statement. The generated arrays are:

# p = [1, 4, 6].
# h = [4, 1, 3].
# x = [2, 5].
# y = [4, 1].
# In Sample Case #2, the generated arrays are:

# p = [2, 4, 6, 8, 10].
# h = [4, 4, 4, 4, 4].
# x = [1, 4, 6, 11, 5].
# y = [3, 5, 3, 3, 1].

inputFile = open('inputFile', 'r')
outputFile = open('outputFile', 'w+')
testCases = int(inputFile.readline())
for t in range(0, testCases):
    z = inputFile.readline()
    if z[len(z) - 1] == '\n':
        z = z[: len(z) - 1]
    line = map(int, z.split(' '))
    n = line[0]
    k=line[1]
    i=0
    p1 = [0]*6
    p2 = [0]*6
    a1=[0]*6
    b1=[0]*6
    c1=[0]*6
    m1=[0]*6
    while i<4:
        z = inputFile.readline()
        if z[len(z) - 1] == '\n':
            z = z[: len(z) - 1]
        line = map(int, z.split(' '))
        p1[i] = line[0]
        p2[i]=line[1]
        a1[i] = line[2]
        b1[i] = line[3]
        c1[i]=line[4]
        m1[i] = line[5]
        i=i+1
    i=2
    p=[0]*n
    p[0] = p1[0]
    p[1] = p2[0]
    h=[0]*n
    h[0] = p1[1]
    h[1] = p2[1]
    x=[0]*k
    x[0] = p1[2]
    x[1] = p2[2]
    y=[0]*k
    y[0] = p1[3]
    y[1] = p2[3]
    while i<n:
        p[i] = (a1[0] * p[i-1] +b1[0]*p[i-2] +c1[0])%m1[0] +1
        h[i] = (a1[1] * h[i - 1] + b1[1] * h[i - 2] + c1[1]) % m1[1] + 1
        i=i+1
    i=2
    while i<k:
        x[i] = (a1[2] * x[i-1] +b1[2]*x[i-2] +c1[2])%m1[2] +1
        y[i] = (a1[3] * y[i - 1] + b1[3] * y[i - 2] + c1[3]) % m1[3] + 1
        i=i+1
    # print p
    # print h
    # print x
    # print y
    i=0
    balloon = 0
    while i<k:
        j=0
        while j<n:
            if x[i] == p[j] and y[i]<=h[j]:
                balloon = balloon + 1
                break
            diff = x[i]-p[j]
            if diff <0:
                diff = p[j] - x[i]
            if h[j] >= y[i] + diff:
                balloon = balloon +1
                break
            else:
                j=j+1
        i=i+1
    outputFile.write('Case #' + str(t + 1) + ": " + str(balloon) + '\n')
inputFile.close()
outputFile.close()


