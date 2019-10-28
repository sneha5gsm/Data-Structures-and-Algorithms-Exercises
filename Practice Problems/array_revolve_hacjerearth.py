def query1(N, Arr, ID, Val):
    ID=ID-1
    i=0
    v = Val - (N - ID)
    total = 0
    # print v
    if ID!=0 and v>0:
        while i<ID and v!=0:
            y = v / N
            l=((y + 1) * v) - (y*(y+1))/2 * N
            # print '**l'
            # print total
            # print l
            total = l + total
            Arr[i] = Arr[i] + total
            i = i + 1
            v = v - 1
    # print Arr
    x = ID - 1
    while ID <N and Val != 0:
        y = Val / N
        l=((y + 1) * Val) - (y*(y+1))/2* N
        total=l + total
        # print total
        Arr[ID] = Arr[ID] + total
        ID = ID + 1
        Val = Val - 1
    while ID<N:
        Arr[ID] = Arr[ID] + total
        ID=ID+1
    # print '------------'
    # print Arr


    # while i<ID:
    # while Val != 0:
    #     if ID == N:
    #         ID = 0
    #         total = Val
    #     Arr[ID] = Arr[ID] + total
    #     ID = ID + 1
    #     Val = Val - 1
    #     total = total + Val
    # while ID < N:
    #     Arr[ID] = Arr[ID] + total
    #     ID = ID + 1

# def query1(N, Arr, ID, Val):
#     ID = ID-1
#     x=ID-1
#     while ID!=x and Val!=0:
#         if ID == N:
#             ID = 0
#         y = Val / N
#         Arr[ID] = Arr[ID] + ((y+1)*Val) - y*N
#         ID = ID + 1
#         Val = Val - 1
#     y = Val / N
#     Arr[ID] = Arr[ID] + ((y+1)*Val) - y*N


def query2(N, Arr, L, R):
    # print 'second  ----'
    # print Arr
    # Write your code here
    ans = 0
    L = L - 1
    R = R - 1
    # print L
    # print R
    if L < R:
        # print L
        # print R
        # print Arr
        if (L - 1) >= 0:
            ans = Arr[R] - Arr[L - 1]
        else:
            ans = Arr[R]
    elif L > R:
        ans = Arr[N - 1] - Arr[L - 1] + Arr[R]
    else:
        if L == 0:
            ans = Arr[0]
        else:
            ans = Arr[R] - Arr[L - 1]
    ans= ans%100000007
    return ans


N, Q = map(int, raw_input().split())
Arr = map(int, raw_input().split())
sumArr = [0] * N
sumArr[0] = Arr[0]
i = 1
# print Arr
while i < N:
    sumArr[i] = sumArr[i - 1] + Arr[i]
    i = i + 1
# print sumArr
for _ in range(Q):
    type, X, Y = map(int, raw_input().split())
    if type == 1:
        query1(N, sumArr, X, Y)
        # print sumArr
    else:
        print (query2(N, sumArr, X, Y))