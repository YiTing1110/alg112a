# x**2 - 3 * x + 1 = 0

a = 1
b = -3
c = 1
x1 = None
x2 = None

discriminant = b**2 - 4 * a * c

if discriminant > 0:
    print("有兩個不相等的實數解")
elif discriminant == 0:
    print("有兩個相等的實數解，這種情況下通常稱為方程有一個重根")
else:
    print("有兩個共軛複數解，即不是實數而是包含虛數部分的解") # ex. x**2 - x + 3

x1 = ((b * -1) + discriminant**(1/2)) / (2 * a)
print(x1)
x2 = ((b * -1) - discriminant**(1/2)) / (2 * a)
print(x2)