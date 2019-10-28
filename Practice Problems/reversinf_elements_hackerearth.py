'''
# Sample code to perform I/O:

name = raw_input()          # Reading input from STDIN
print 'Hi, %s.' % name      # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n, q = map(int, raw_input().split())
old_list = map(int, raw_input().split())
tupleArr = [0] * n
tupleArrRev = [0] * n
j = 1
sum1 = old_list[0]
maximum = old_list[0]
tupleArr[0] = (old_list[0], old_list[0])
while j < n:
    if (old_list[j] + sum1) > old_list[j]:
        sum1 = old_list[j] + sum1
    else:
        sum1 = old_list[j]
    if sum1 > maximum:
        maximum = sum1
    tupleArr[j] = (sum1, maximum)
    j = j + 1
j=n-1
sum1 = -1000001
maximum = -100001
tupleArrRev[0] = (-100001, -1000001)
while j >=0:
    if (old_list[j] + sum1) > old_list[j]:
        sum1 = old_list[j] + sum1
    else:
        sum1 = old_list[j]
    if sum1 > maximum:
        maximum = sum1
    tupleArrRev[j] = (sum1, maximum)
    j = j - 1
i = 0
# print tupleArr
# print tupleArrRev
while i < q:
    arr = old_list[:]
    # print arr
    l, r = map(int, raw_input().split())
    if (n-r)>(l-1):
        # print 'inside iffff***'
        l = l - 1
        r = r - 1
        j=n-1
        sum1= tupleArrRev[r + 1][0]
        maximum = tupleArr[r + 1][1]
        j=l
        while j<=r:
            if (arr[j] + sum1) > arr[j]:
                sum1 = arr[j] + sum1
            else:
                sum1 = arr[j]
            if sum1 > maximum:
                maximum = sum1
            j=j+1
        j=l-1
        while j>=0:
            if (arr[j] + sum1) > arr[j]:
                sum1 = arr[j] + sum1
            else:
                sum1 = arr[j]
            if sum1 > maximum:
                maximum = sum1
            j=j-1
        i=i+1
        print maximum
    else:
        # print 'inisde elseeee'
        l = l - 1
        r = r - 1
        j = r
        if l > 0:
            sum1 = tupleArr[l - 1][0]
            maximum = tupleArr[l - 1][1]
        else:
            sum1 = 0
            maximum = -1000001
        while j >= l:
            if (arr[j] + sum1) > arr[j]:
                sum1 = arr[j] + sum1
            else:
                sum1 = arr[j]
            if sum1 > maximum:
                maximum = sum1
            j = j - 1
        j = r + 1
        while j < n:
            if (arr[j] + sum1) > arr[j]:
                sum1 = arr[j] + sum1
            else:
                sum1 = arr[j]
            if sum1 > maximum:
                maximum = sum1
            j = j + 1
        i = i + 1
        print maximum