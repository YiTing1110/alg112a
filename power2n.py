from datetime import datetime

# 方法 1
def power2n_1(n):
    return 2**n

# 方法 2a：用遞迴
def power2n_2(n):
    if n == 0: return 1
    return power2n_2(n-1) + power2n_2(n-1)

# 方法2b：用遞迴
def power2n_3(n):
    if n == 0: return 1
    return 2 * power2n_3(n-1)

# 方法 3：用遞迴+查表
p = [None]*1000
p[0] = 1
def power2n_4(n):
    if p[n] != None: return p[n]
    p[n] = power2n_4(n-1) + power2n_4(n-1)
    return p[n]

n = 10

startTime = datetime.now()

print(power2n_1(n))

endTime = datetime.now()
seconds = endTime - startTime
print(f'time:{seconds}')

startTime = datetime.now()

print(power2n_2(n))

endTime = datetime.now()
seconds = endTime - startTime
print(f'time:{seconds}')

startTime = datetime.now()

print(power2n_3(n))

endTime = datetime.now()
seconds = endTime - startTime
print(f'time:{seconds}')

startTime = datetime.now()

print(power2n_4(n))

endTime = datetime.now()
seconds = endTime - startTime
print(f'time:{seconds}')