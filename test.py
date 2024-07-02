import random


def line_generation(count1, count2, count3):
    resault = []

    for i in range(count1): resault.append(1)
    for i in range(count2): resault.append(2)
    for i in range(count3): resault.append(3)
    for i in range(count1 + count2 + count3): resault.append(0)
    
    random.shuffle(resault)

    return resault

print(line_generation(5, 4, 6))
