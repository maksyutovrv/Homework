# Hard level
name = input('Введите свое имя: ')
surname = input('Введите свою фамилию: ')
age = int(input('Введите свой возраст: '))
weight = int(input('Введите свой вес: '))
if age < 30 and 50 < weight < 120:
    print(name, surname, ', возраст', age, ', вес ', weight, '- Вы в отличной форме')
elif 30 < age < 40 and weight < 50 or weight > 120:
    print(name, surname, ', возраст', age, ', вес ', weight, '- Вам следует вести правильный образ жизни')
elif age > 40 and weight < 50 or weight > 120:
    print(name, surname, ', возраст', age, ', вес ', weight, '- Вам бы пройти врачебный осмотр')
else:
    print(name, surname, ', возраст', age, ', вес ', weight, '- Рекомендовано не заморачиваться!')