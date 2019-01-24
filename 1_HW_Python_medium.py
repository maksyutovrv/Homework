# Medium level
# Task 1
number = int(input('Введите случайное число от 0 до 10: '))
while number > 10:
    number = int(input('Число неверное, введите значение от 0 до 10: '))
else:
    number = number ** 2
print(number)

# Task 2
a = 10
b = 20
print ('Значение а до:',a, 'Значение b до:',b)
a = a + b
b = a - b
a = a - b
print('Значение а после:',a, 'Значение b после:',b)
