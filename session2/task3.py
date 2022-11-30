import random
N = random.randrange(2,10)
a = [random.randrange(-5,6) for i in range(N)]
print("N = ", N)
print("Array:\n",a)
M = 0
for x in a :
    if x < 0 :
        M += 1
print("Modified Array 2:\n",a)
print("Length:\n",len(a))