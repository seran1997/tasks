# Задача
# Пусть Анфиса посчитает кое-что про нашу компанию друзей:
# Напишите функцию подсчета общего возраста друзей, которая принимает на вход список возрастов, а возвращает число — общий возраст друзей.
# Напишите функцию подсчета среднего возраста друзей, которая принимает на вход список возрастов, а возвращает число — средний возраст друзей.

print("Привет, я Анфиса!")
friends = ['Сергей', 'Соня', 'Дима', 'Алина', 'Егор']
friends_ages = [20, 19, 31, 33, 25]


def total_age(ages):
    total_age=0
    for age in ages:
        total_age+=age
    return total_age


def mean_age(ages):
    count=0
    for age in ages:
        count+=1
    return total_age(ages)/count


def print_ages_info():
    print('Общий возраст друзей:', total_age(friends_ages))
    print('Средний возраст друзей:', mean_age(friends_ages))
print_ages_info()