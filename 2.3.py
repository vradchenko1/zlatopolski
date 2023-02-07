# тут синусы есть
# a)
import math
a = int(input('Введите значение a:'))
sin = math.sin(3 * a)
a1 = 2 * a + sin
sqrt = math.sqrt(a1 / 3.56)
print(sqrt)

# б)
x = int(input('Введите значение x: '))
sqrt = math.sqrt(1 + x)
y = 3.2 + sqrt / abs(5 * x)
print(y)