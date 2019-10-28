n = int(raw_input())
names = []
alpha={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
dict={}
for a0 in xrange(n):
    name = raw_input().strip()
    names.append(name)
    dict[name] = 0
names = sorted(names)
i=0
while i<n:
    dict[names[i]] = i+1
    i=i+1
q = int(raw_input())
for a0 in xrange(q):
    name = raw_input().strip()
    i=0
    x=len(name)
    i=0
    sum=0
    while i<x:
        # print alpha[name[i]]
        sum=sum+alpha[name[i]]
        i=i+1
    sum=sum*dict[name]
    print sum
