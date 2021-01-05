import numpy as np
F = [1,2]
ans = 2
while True:
    tmp = F[-1]+F[-2]
    if tmp > 4000000:
        break
    F.append(tmp)
    if tmp % 2 == 0:
        ans += tmp
print(ans)