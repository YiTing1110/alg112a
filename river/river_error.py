# human wolf sheep cabbage
river = [0, 0, 0, 0]
step = [[0, 0, 0, 0]]
alone = True

def die():
    if river[0] ^ river[2]:
        if not(river[1] ^ river[2]) or not(river[2] ^ river[3]):
            return False
        step.append(river.copy())
        return True

for i in river[1:4]:
    river[0] = river[0] ^ 1
    if die() and step[-1] != step[-2]: pass
    #elif not(die()):


if river[0:4] == [1, 1, 1, 1]:
    print("Step:", step)
    exit()