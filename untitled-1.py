import time
import random
c = int(input())
a1 = [0] * (c // 2) + [1] + [0] * (c // 2)   # [random.randint(0, 1) for i in range(c)]
print(a1)   #
b = int(input())
for j in range(b):
    a2 = [0] * c
    for i in range(c):
        if (a1[i - 1] == 1 and a1[(i + 1) - (i + 1) // c] == 1) or a1[i - 1] == 0 and a1[(i + 1) - ((i + 1) // c) * c] == 0:
            a2[i] = 0
        elif a1[i - 1] == 1 or a1[(i + 1) - ((i + 1) // c) * c] == 1:
            a2[i] = 1
    time.sleep(0.5)
    print("".join(str(i) if i == 1 else " " for i in a1))
    a1 = a2.copy()
    
    
    
# ⏘
# ⏤
    