
arr = [9, 6, 5, 2, 3]

def addElement(value):
    arr.append(value)
    percup(len(arr) - 1)

def percup(self, i):
    while i>=0:
        x = (i-1)//2
        if arr[i] > arr[(i-1)//2]:
            temp = arr[i]
            arr[i] = arr[x]
            arr[x] = temp
        i = (i-1)//2

def delElement():
    i = len(arr) - 1
    arr[0] = arr[i]
    percdown(0)
    arr.pop()

def percdown(i):
    size = len(arr)
    print('inside percdown')
    print(i)
    while (i*2 + 2)< size:
        m = minChild(i)
        print('m: '+ str(m))
        if arr[i] > arr[m]:
            temp = arr[i]
            arr[i] = arr[m]
            arr[m] = temp
        i = m

def minChild(i):
    if (2*i + 2) > (len(arr) - 1):
        return 2*i + 1
    if arr[2*i + 1] > arr[2*i + 2]:
        return 2*i +2
    else:
        return 2*i +1



def buildHeap():
    i=(len(arr)-2)//2
    while i>=0:
        percdown(i)
        i=i-1
    print(arr)

buildHeap()



