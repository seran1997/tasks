# Объявите функцию process_friend(name, query), принимающую имя друга name и запрос query. В этой функции будут обрабатываться запросы, в которых имя — не «Анфиса».
# В функции process_friend() напишите ветвление:
# если друг с именем name есть в словаре DATABASE:
# если переменная query содержит строку 'ты где?' — функция должна вернуть сообщение '{имя_друга} в городе {название_города}'; название города нужно получить из словаря DATABASE;
# если переменная query содержит какую-то другую строку — функция должна вернуть сообщение <неизвестный запрос>.
# если друга с именем name нет в словаре DATABASE — функция должна вернуть сообщение: У тебя нет друга по имени {имя_друга}.
# Теперь нужно дописать функцию process_query(). 
# Добавьте в ветвление if name == 'Анфиса' блок else: если запрос начинается не с имени «Анфиса» — верните результат вызова функции process_friend(), передав в неё два аргумента: имя друга и текст вопроса. 
# Добавьте новые вызовы функции process_query():
# print(process_query('Коля, что делать?'))
# print(process_query('Антон, ты где?')) 

DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}

# Новая функция, она возвращает правильное словосочетание, склоняя слово "друзья" 
# в зависимости от того, какое число передано в аргументе friends_count
def format_friends_count(friends_count):
    if friends_count == 1:
        return '1 друг'
    elif 2 <= friends_count <= 4:
        return f'{friends_count} друга'
    else:
        return f'{friends_count} друзей'


def process_anfisa(query):
    if query == 'сколько у меня друзей?':
        count = len(DATABASE)
        # Вызовите функцию format_friends_count() и передайте в неё count.
        # Отредактируйте строку ниже: в ней должно использоваться выражение, 
        # которое вернёт функция format_friends_count()
        return f'У тебя {format_friends_count(count)}.'
    elif query == 'кто все мои друзья?':
        friends_string = ', '.join(DATABASE)
        return f'Твои друзья: {friends_string}'
    elif query == 'где все мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        return f'Твои друзья в городах: {cities_string}'
    else:
        return '<неизвестный запрос>'

def process_query(query):
    qr=query.split(', ')
    if qr[0]=='Анфиса':
        return process_anfisa(qr[1])
    else:
        return process_friend(qr[0],qr[1])
def process_friend(name, query):
    if name in DATABASE:
        if query=='ты где?':
            city=DATABASE[name]
            return f'{name} в городе {city}'
        else:   
            return '<неизвестный запрос>'  
    else:   
            return f'У тебя нет друга по имени {name}'
print('Привет, я Анфиса!')
print(process_query('Анфиса, сколько у меня друзей?'))
print(process_query('Анфиса, кто все мои друзья?'))
print(process_query('Анфиса, где все мои друзья?'))
print(process_query('Анфиса, кто виноват?'))
print(process_query('Соня, ты где?'))
print(process_query('Коля, что делать?'))
print(process_query('Антон, ты где?')) 