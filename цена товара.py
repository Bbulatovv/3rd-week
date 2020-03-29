x = float(input())
k = round((x - int(x)) * 100)
r = round(x - (k / 100))
print(r, k)
