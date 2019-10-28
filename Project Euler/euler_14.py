t = int(raw_input())
done={1:0}
def recursiveFn(n):
    if n in done.keys():
        return done[n]
    else:
        total=0
        if n%2 ==0:
            total = 1 +recursiveFn(n/2)
        else:
            total = 1 + recursiveFn(3*n+1)
        done[n] = total
        return total
for a0 in xrange(t):
    n = int(raw_input().strip())
    i= n-1
    maximum=0
    ans =1
    while i>1:
        m=recursiveFn(i)
        if m> maximum:
            maximum=m
            ans =i
        if m<maximum:
            break
        i=i-1
    print ans
