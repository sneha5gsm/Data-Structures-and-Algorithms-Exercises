e=2.71828
ts = int(raw_input().strip())
facts=[0, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
for x in range(ts):
    digits={}
    n = raw_input().strip()
    l=len(n)
    i=0
    while i <l:
        digits[n[i]] = 1
        i=i+1
    x=len(digits)
    total = int(facts[x]*e)
    print total
