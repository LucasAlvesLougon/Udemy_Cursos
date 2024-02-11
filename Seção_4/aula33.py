from itertools import count

c1 = count(1)
for i in c1:
    if i > 100:
        print(i)
        break