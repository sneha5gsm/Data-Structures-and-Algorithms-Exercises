def query1(N, Arr, ID, Val):
    ID = ID-1
    x=ID-1
    while ID!=x and Val!=0:
        if ID == N:
            ID = 0
        y = Val / N
        Arr[ID] = Arr[ID] + ((y+1)*Val) - y*N
        ID = ID + 1
        Val = Val - 1
    y = Val / N
    Arr[ID] = Arr[ID] + ((y+1)*Val) - y*N
    # print Arr



def query2(N, Arr, L, R):
    ans = 0
    L = L - 1
    R = R - 1
    # print '---- second'
    # print L
    # print R
    while L!=R:
        if L==N:
            L=0
        else:
            ans = ans + Arr[L]
            L=L+1
        # print L
    ans = ans+Arr[R]
    ans = ans%1000000007
    return ans


N, Q = map(int, raw_input().split())
Arr = map(int, raw_input().split())
i = 1

for _ in range(Q):
    type, X, Y = map(int, raw_input().split())
    if type == 1:
        query1(N, Arr, X, Y)
        # print sumArr
    else:
        print (query2(N, Arr, X, Y))