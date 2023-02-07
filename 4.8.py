#  Составить программу для вычисления значения функции

import math
x = int(input('x = '))
sin = math.sin(x)

if sin >= 0:
    k = x ** 2
else:
        k = abs(x)

if x >= k:
    f = k * x
else:
        f = abs(x)


print('f(x) = ', f)