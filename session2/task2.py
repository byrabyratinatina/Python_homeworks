N = int(input('Введите число больше нуля '))

f = 1
for i in range(1, N+1):
    
    f = i * f
    
    print(f, end=" ")