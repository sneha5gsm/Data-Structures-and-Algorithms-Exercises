import math

N, Q = map(int, raw_input().split())
A = map(int, raw_input().split())
checklist ={}
i = 1
q=math.log(N,2)
if int(q) ==q:
    v=int(q)
else:
    v=int(q)+1
w = int(2 *(math.pow(2,v) -1)) +1
# print w
tree = [0]* (w)

def build(node, start, end):
    if start == end:
        checklist[start] = node
        tree[node] = A[start]
    else:
        mid = (start + end) / 2
        build(2*node +1, start, mid)
        build(2*node+2, mid+1, end)
        tree[node] = tree[2*node+1] + tree[2*node+2]
    # print tree

# def update(node, start, end, idx, val):
#     if start == end:
#         A[idx] += val
#         tree[node] += val
#     else:
#         mid = (start + end) / 2
#         if start <= idx and idx <= mid:
#             update(2*node+1, start, mid, idx, val)
#         else:
#             update(2*node+2, mid+1, end, idx, val)
#         tree[node] = tree[2*node+1] + tree[2*node+2]

def update(node , start, end, idx, val):
    i=0
    j=w-1
    x=v
    # print '-----**'
    # print v
    # print j
    while i<v:
        k=0
        while k<math.pow(2,x):
            if tree[j]!=0 and tree[j-1]!=0:
                tree[(j-2)/2] =  tree[j] + tree[j-1]
            j=j - 2
            k=k+2
        x=x-1
        i=i+1
    # print tree

def query(node, start, end, l, r):
    if r < start or end < l:
        return 0
    if l <= start and end <= r:
        return tree[node]
    mid = (start + end) / 2
    p1 = query(2*node+1, start, mid, l, r)
    p2 = query(2*node+2, mid+1, end, l, r)
    return p1 + p2


def query1(N, Arr, ID, Val):
    # print '-------'
    ID = ID-1
    x=ID-1
    while ID!=x and Val!=0:
        if ID == N:
            ID = 0
        y = Val / N
        z =((y+1)*Val) - ((y*(y+1))/2)*N
        tree[checklist[ID]] = tree[checklist[ID]] + z
        # update(0,0,N-1,ID, z)
        # print z
        # print ID
        # print tree
        ID = ID + 1
        Val = Val - 1
    y = Val / N
    z=((y+1)*Val) - ((y*(y+1))/2)*N
    tree[checklist[ID]] = tree[checklist[ID]] + z
    update(0, 0, N - 1, ID, z)
    # print z
    # print ID
    # print tree
    # print tree


build(0,0,N-1)
# print tree


for _ in range(Q):
    type, X, Y = map(int, raw_input().split())
    if type == 1:
        query1(N, A, X, Y)
        # print sumArr
    else:
        # print tree
        if X<=Y:
            x=query(0,0,N-1,X-1, Y-1)
        else:
            x=query(0,0,N-1,X-1, N-1) + query(0,0,N-1,0, Y-1)
        x=x%1000000007
        print x