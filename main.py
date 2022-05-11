import random
def cake():
    c1 = random.randint(0, 100)
    c2 = random.randint(0, 100)
    k = random.randint(0, 100)
    if c1 < k < c2 or c2 < k < c1:
        return True
    else:
        return False

i = int(input("Itterations? "))
cut = 0
for a in range(1, i+1):
    if cake():
        cut += 1
    print(a, cut, cut/a)
