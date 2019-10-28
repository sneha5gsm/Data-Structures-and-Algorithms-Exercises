# Enter your code here. Read input from STDIN. Print output to STDOUT
def f(x):
    return {
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '0': 0,
    }[x]
t = int(raw_input())
factorials={0:1,1:1}
for a0 in xrange(t):
    n = int(raw_input())
    if n in factorials:
        print str(factorials[n])
    else:
        i=n
        fact=1
        while i>0:
            if i in factorials:
                fact = fact * factorials[i]
                break
            else:
                fact = fact *i
                i=i-1
        t=str(fact)
        l=len(t)
        i=0
        sum=0
        while i<l:
            sum= sum+ f(t[i])
            i=i+1
        print str(sum)