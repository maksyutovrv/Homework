# Создайте программу медицинская анкета, где вы запросите у пользователя такие данные, как имя, фамилию, возраст, и вес.
# И выведите результат согласно которому пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
# Пациенту требуется начать вести правильный образ жизни, если ему более 30 и вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
# Все остальные варианты вы можете обработать на ваш вкус и полет фантазии =)
name = input('Введите свое имя: ')
surname = input('Введите свою фамилию: ')
age = int(input('Введите свой возраст: '))
weight = int(input('Введите свой вес: '))
if age < 30 and 50 < weight < 120:
    print(name, surname, ', возраст', age,', вес ',weight,'- Вы в отличной форме')
elif 30 < age < 40 and weight < 50 or weight > 120:
    print(name, surname, ', возраст', age,', вес ',weight,'- Вам следует вести правильный образ жизни')
elif age > 40 and weight < 50 or weight > 120:
    print(name, surname, ', возраст', age,', вес ',weight,'- Вам бы пройти врачебный осмотр')
else:
    print(name, surname, ', возраст', age,', вес ',weight,'- Рекомендовано не заморачиваться!')
