studs = sorted(studs, key=lambda x: x[1])
studs.reverse()
i=0
j=i
# print studs
while i<n:
    start = i
    while i<(n-1) and studs[i][1] == studs[i+1][1]:
        # print 'inisde id '
        i=i+1
    if start !=i:
        # print 'ininn'
        studs = studs[:start] + sorted(studs[start:i+1], key=lambda x: x[0]) + studs[i+1:]
        # print start
        # print i
        # print studs
    i=i+1