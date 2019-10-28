
from itertools import permutations
assumption = {4:[[1,1,2]], 5:[[2,1,2]], 6:[[1,2,3]], 7:[[2,2,3],[1,3,3]], 8:[[2,2,4],[2,3,3],[3,1,4]], 9:[[2,3,4], [4,1,4]]}
done={}
n = int(raw_input().strip())
i=1
s = ''
total =0
while i<=n:
    s= s+str(i)
    i=i+1
# print s
allPerms = [''.join(p) for p in permutations(s)]
# print allPerms
i=0
l=len(allPerms)
while i<l:
    j=0
    while j<len(assumption[n]):
        x=assumption[n][j]
        a=int(allPerms[i][:x[0]])
        b=int(allPerms[i][x[0]:x[0]+x[1]])
        c = int(allPerms[i][x[0] + x[1]:])
        if  (a*b)==c:
            if c in done.keys():
                flag=0
            else:
                # print '---'
                # print c
                total = total + c
                done[c] =1
        j=j+1
    i=i+1
print total

