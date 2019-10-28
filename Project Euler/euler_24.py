# Enter your code here. Read input from STDIN. Print output to STDOUT
alpha={1:'a',2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g',8:'h', 9:'i', 10:'j', 11:'k', 12:'l', 13:'m'}
fact={1:1, 2: 2, 3:6, 4:24, 5:120, 6:720, 7:5040, 8:40320, 9:362880, 10: 3628800, 11:39916800 , 12: 479001600}
t = int(raw_input())
for a0 in xrange(t):
    n = int(raw_input().strip())
    n=n-1
    # print '-------------'
    # print n
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
    # print letters
    ans = ''
    x=12
    while n>-1:
        y=n/fact[x]
        # print y
        ans = ans+ letters[y]
        # print ans
        del letters[y]
        # print letters
        # print '====='
        n = n%fact[x]
        if n==0:
            i=0
            l=len(letters)
            while i<l:
                ans = ans + letters[i]
                i=i+1
            break
        x=x-1
    print ans

