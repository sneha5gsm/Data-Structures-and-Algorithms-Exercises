# ##################### Question ######################
# A "0/1 string" is a string in which every character is either 0 or 1. There are two operations that can be performed on a 0/1 string:

# switch: Every 0 becomes 1 and every 1 becomes 0. For example, "100" becomes "011".
# reverse: The string is reversed. For example, "100" becomes "001".
# Consider this infinite sequence of 0/1 strings:

# S0 = ""

# S1 = "0"

# S2 = "001"

# S3 = "0010011"

# S4 = "001001100011011"

# ...

# SN = SN-1 + "0" + switch(reverse(SN-1)).

# You need to figure out the Kth character of Sgoogol, where googol = 10100.

# Input
# The first line of the input gives the number of test cases, T. Each of the next T lines contains a number K.

# Output
# For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is the Kth character of Sgoogol.

# Limits
# 1 ≤ T ≤ 100.
# Small dataset
# 1 ≤ K ≤ 105.
# Large dataset
# 1 ≤ K ≤ 1018.
# Sample

# Input 
 	
# Output 
 
# 4
# 1
# 2
# 3
# 10

# Case #1: 0
# Case #2: 0
# Case #3: 1
# Case #4: 0



# done
inputFile = open('inputFile', 'r')
outputFile = open('outputFile', 'w+')
testCases = int(inputFile.readline())
for t in range(0, testCases):
    k = int(inputFile.readline())
    # print len(bin(k)[2:])
    binary = bin(k)[2:]
    logTwo = len(binary)
    if binary.count('1') == 1:
        fileLine = 'Case #' + str(t + 1) + ": " + '0' + '\n'
        outputFile.write(fileLine)
    else:
        output = '0'
        x = pow(2, logTwo)
        while k>0:
            y = x/2
            if k == y:
                break
            if k > y:
                output = '1'
                k = k - y
            else:
                output = '0'
            x = y
        fileLine = 'Case #' + str(t + 1) + ": " + output + '\n'
        outputFile.write(fileLine)
inputFile.close()
outputFile.close()
