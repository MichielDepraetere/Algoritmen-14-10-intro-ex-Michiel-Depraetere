def specificSummator():
    counter = 0
    for i in range(0, 10000):
        if (i % 7) == 0:
            counter += i
        elif (i % 9) == 0:
            counter += i
    return counter

print(specificSummator())