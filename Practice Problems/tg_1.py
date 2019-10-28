def binarySearch(arr, l, r, x, n):
    print('inside')
    if r >= l:
        print('inside 2')
        print('l: ' +str(l))
        mid = l + (r -1 ) // 2
        print('r: ' + str(r))
        print('mid: ' + str(mid))
        if l==r:
            if arr[l]<=x:
                return l+1
            else:
                return l
            return l+1
        # if mid == (n - 1):
        #     if arr[mid] < x:
        #         return n
        #     else:
        #         return n-1
        #     print('herttttttttttttttt')
        #     return str(n)
        elif mid == 0:
            if arr[mid]>x:
                return 0
            else:
                return binarySearch(arr, 1, r, x, n)
            # if arr[]
            print('mid:   ' +str(mid))
            print('insideeeeeeeeeeeeeeeee')
            return mid
        else:
            if arr[mid - 1] <= x:
                if arr[mid] > x:
                    print('hereeeeeeeeeeeeeee')
                    return str(mid)
                else:
                    return binarySearch(arr, mid + 1, r, x, n)
            else:
                return binarySearch(arr, l, mid - 1, x, n)

y =binarySearch([0.0, 5.0],0 ,1, 10, 2)
print(y)
def return_val(a):
    return 0

print(return_val(0))


print(len('1.1'))

''' Read input from STDIN. Print your output to STDOUT '''
# Use input() to read input from STDIN and use print to write your output to STDOUT
import math


def binarySearch(arr, l, r, x, n):
    if r >= l:

        mid = l + (r - l) // 2
        if l == r:
            if arr[l] <= x:
                return l + 1
            else:
                return l
            return l + 1
        elif mid == 0:
            if arr[mid] > x:
                return 0
            else:
                return binarySearch(arr, 1, r, x, n)
            return mid
        else:
            if arr[mid - 1] <= x:
                if arr[mid] > x:
                    return mid
                else:
                    return binarySearch(arr, mid + 1, r, x, n)
            else:
                return binarySearch(arr, l, mid - 1, x, n)


def main():
    ts = int(input())

    for t in range(ts):
        l = int(input())
        arr = [0] * l
        for i in range(l):
            arr[i] = tuple(int(x.strip()) for x in input().split(' '))
        distances = [[0.00] * l for i in range(l)]
        # print(distances)
        # print(arr)
        ans = []
        for i in range(l):
            for j in range(i + 1, l):
                # print(i)
                # print(j)
                # print('--')
                x = math.sqrt(math.pow(arr[i][0] - arr[j][0], 2) + math.pow(arr[i][1] - arr[j][1], 2))
                distances[i][j] = x
                distances[j][i] = x
        for i in range(l):
            distances[i].sort()
            distances[i] = distances[i][1:]
            j = (l - 2) // 2
            limit = distances[i][0] * 2
            z = binarySearch(distances[i], 0, l - 2, limit, l - 1)
            y = round(distances[i][0], 2)
            if len(str(y)) < 4:
                print(str(y) + '0' + ' ' + str(z))
            else:
                print(str(y) + ' ' + str(z))
            # ans.append((distances[i][0], binarySearch(distances[i], 0, l-2, limit, l-1)))

        # print(distances)


# Write code here

main()

