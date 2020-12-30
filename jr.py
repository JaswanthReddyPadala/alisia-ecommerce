oplis = []
def add(num):
    s = 0
    num=str(num)
    for i in num:
        s+=int(i)
    if s>=10:
        s = add(s)
    else:
        return s

for i in range(1000, 10000):
    p = str(i)
    c = 0
    for j in range(0, 3):
        if p[j] < p[j+1]:
            c += 1
    s = add(p)
    if s == 8 and c == 3:
        oplis.append(i)
print(oplis)
print(add(2357))