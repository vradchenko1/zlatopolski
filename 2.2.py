# Составить программу вычисления значения функции при любом значении а. 

import math

a = int(input(''))
sqrt = math.sqrt(a * a + 1)
y = a * a + 1 / sqrt
print(y)