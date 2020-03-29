n = int(input())
Sum = 0.0
i = 1
for i in range(1, n + 1):
    s = 1.0 / (i**2)
    Sum += s
    i = i + 1
print(Sum)
