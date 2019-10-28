def recursiveFn(arr, k, count, done):
    n=len(arr)
    x=count
    # print 'arr in fn'
    # print arr
    if n==0 or n==1:
        # print 'inside if'
        return count, done
    if str(arr) in done.keys():
        # print 'inside'
        return count + done[str(arr)], done
    else:
        i=1
        while i<n:
            # print 'arr 0 and arr i'
            # print arr[i]
            # print i
            if (arr[i] - arr[0]) >= k:
                # print 'inside if cond'
                c, r =recursiveFn(arr[i:], k, x+1, done)
                count = max(count, c)
                # print count
            i=i+1
        done[str(arr)] = count -x
        return count, done


k= int(raw_input())
n=int(raw_input())
z = raw_input()
if z[len(z) - 1] == '\n':
    z = z[: len(z) - 1]
arr = map(int, z.split(' '))
# print arr
i=0
count =1
done={}
while i<(n-1):
    c, r = recursiveFn(arr[i:], k, 1, done)
    count = max(count, c)
    done = r
    i=i+1
print count

'''
# Sample code to perform I/O:

name = raw_input()          # Reading input from STDIN
print 'Hi, %s.' % name      # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
import numpy as np

# Write your code here
ts = int(raw_input())
for t in range(0, ts):
    n, k = raw_input().split()
    n, k = [int(n), int(k)]
    z = raw_input()
    if z[len(z) - 1] == '\n':
        z = z[: len(z) - 1]
    arr = map(int, z.split(' '))
    if n == k:
        print 'YES'
    else:
        x = np.array(arr)
        uniques = np.unique(x)
        arr2 = []
        # print uniques

        if len(uniques) > k:
            print 'NO'
        else:
            i = 0
            flag = 0
            mins = arr.count(uniques[0])
            while i < len(uniques):
                x = arr.count(uniques[i])
                arr2.append(x)
                if x < mins:
                    mins = x
                i = i + 1
            while i < len(uniques):
                if uniques[i] % mins != 0:
                    flag = 1
                    break
                i = i + 1
            if flag == 1:
                print 'NO'
            else:
                print 'YES'
