# Дано двузначное число. Найти:
# а) число десятков в нем;

num = int(input('Введите двузначное число: '))
d = num // 10
print(d, ' - десятки')

# б) число единиц в нем.

ed = num % 10
print(ed, ' - единиц')