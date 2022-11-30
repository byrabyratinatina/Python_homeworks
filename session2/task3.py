import random
N = random.randrange(2,10)
a = [random.randrange(-5,6) for i in range(N)]
print("N = ", N)
print("Array:\n",a)
M = 0
for x in a :
    if x < 0 :
        M += 1
a.extend([0]*M)
j = 0
for i in range(N-1,-1,-1) :
    if a[i] < 0 :
        a[(N+M-1)-j] = 0
        j += 1
    a[(N+M-1)-j] = a[i]
    j += 1
print("Modified Array 2:\n",a)
print("Length:\n",len(a))