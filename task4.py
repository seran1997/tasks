# Упростим и улучшим код Анфисы. 
# При выводе перечня друзей или городов Анфиса применяет циклы, объединяя ключи или значения словаря в одну строку, через пробел. 
# Но теперь в вашем арсенале есть метод join(), он решает ту же задачу: создаёт строку из элементов последовательности.
# Уберите из кода циклы, в которых создаётся перечень друзей и перечень городов, а эти перечни создайте с помощью метода join(). Имена друзей и названия городов должны быть разделены запятыми и пробелом.
# # Анфиса должна вернуть примерно такие строки:
# # В ответ на запрос 'Кто все мои друзья?'-
# Твои друзья: Серёга, Соня, Миша, ...

# В ответ на запрос 'Где все мои друзья?' -
#Твои друзья в городах: Омск, Москва, Челябинск, ... 
#Для начала разделить ключи и значения, после при помощи метода join склеить и вывести
DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}

def process_anfisa(query):
    if query == 'Сколько у меня друзей?':
        count = len(DATABASE)
        
        return 'У тебя ' + str(count) + ' друзей.'
    elif query == 'Кто все мои друзья?':
        # Из словаря DATABASE создайте строку с помощью join();
        # имена друзей разделите запятой и пробелом.
        # Запишите эту строку в переменную friends_string (вместо пустых кавычек).
        friends_string = ', '.join(DATABASE.keys())

        return 'Твои друзья: ' + friends_string
    elif query == 'Где все мои друзья?':
        unique_cities = set(DATABASE.values())
        # Из сета unique_cities создайте строку с помощью join();
        # названия городов разделите запятой и пробелом.
        # Запишите эту строку в переменную cities_string (вместо пустых кавычек).
        cities_string = ', '.join(unique_cities)

        return 'Твои друзья в городах: ' + cities_string
    else:
        return '<неизвестный запрос>'


print('Привет, я Анфиса!')
print(process_anfisa('Сколько у меня друзей?'))
print(process_anfisa('Кто все мои друзья?'))
print(process_anfisa('Где все мои друзья?'))
