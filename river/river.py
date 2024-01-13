# 《狼、羊、甘藍菜》過河的問題
# 未使用演算法

from datetime import datetime

initial = ["wolf", "sheep", "cabbage"]
right = []
left = []

def foodChain(animal):
    if animal[0] == "cabbage":
        if animal[1] == "sheep":
            return 1
    elif animal[0] == "wolf":
        if animal[1] == "sheep":
            return 1
    else: # sheep
        return 1
    return 0
    
# 把 a 送到 b
def send(a, b):
    print("sent:", a[0])
    b.append(a[0])
    a.pop(0)

def main():
    left.clear()
    right = initial.copy()
    print("initial", initial)
    while len(right) != 0:
        send(right, left)
        print("right: ", right, "\t left", left)
        if len(left) == 2 and foodChain(left) == 1 or len(right) == 2 and foodChain(right) == 1:
            send(left, right)
            print("right: ", right, "\t left", left)

main()