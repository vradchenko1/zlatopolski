# Рассчитать значение у при заданном значении х
import math
x = int(input('x = '))
if x > 0:
    y = (math.sin(x)) ** 2

else:
        y = 1 - 2 * (math.sin(x)) ** 2

print('y = ', y)