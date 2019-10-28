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
n = int(raw_input())
i=0
sum =0
while i<n:
    sum= sum+ int(raw_input().split())
    i=i+1
i=0
s=0
sumString = str(sum)
while i<10:
    s = s+f(sumString[0])
    i=i+1
print s