n = 5
ans = 1
n1 = n2 = 1
if n < 3:
    ans = 1
else:
    for i in range(n - 2):
        n2 = n1
        n1 = ans
        ans = n1 + n2
print(ans)