n = int(input("монетки > "))
res = n // 2
if n % 2 == 1:
    res += 1
print(res)