# Применить все полученные в этой теме знания, чтобы научить Анфису отвечать на вопросы про друзей, сколько у них сейчас времени:
# Артём, который час?
# Антон, который час?
# Примеры таких запросов уже добавлены в список queries в функции runner().
# Измените функцию process_friend(), чтобы она обрабатывала ещё один запрос, а именно query == 'который час?'.
# Если город друга есть в базе UTC_OFFSET, вызовите функцию what_time() и, подставив полученный результат, верните ответ в формате Там сейчас 19:28.
# Если город отсутствует в базе UTC_OFFSET, то верните сообщение об ошибке <не могу определить время в городе {название}>.
import datetime as dt
DATABASE = {
    'Сергей': 'Омск',
    'Соня': 'Москва',
    'Алексей': 'Калининград',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск',
    'Артём': 'Владивосток',
    'Петя': 'Михайловка'
}

UTC_OFFSET = {
    'Москва': 3,
    'Санкт-Петербург': 3,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казань': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Самара': 4,
    'Ростов-на-Дону': 3,
    'Уфа': 5,
    'Красноярск': 7,
    'Воронеж': 3,
    'Пермь': 5,
    'Волгоград': 3,
    'Краснодар': 3,
    'Калининград': 2,
    'Владивосток': 10
}


def format_count_friends(count_friends):
    if count_friends == 1:
        return '1 друг'
    elif 2 <= count_friends <= 4:
        return f'{count_friends} друга'
    else:
        return f'{count_friends} друзей'


def what_time(city):
    offset = UTC_OFFSET[city]
    city_time = dt.datetime.utcnow() + dt.timedelta(hours=offset)
    f_time = city_time.strftime("%H:%M")
    return f_time


def process_anfisa(query):
    if query == 'сколько у меня друзей?':
        count = len(DATABASE)
        return f'У тебя {format_count_friends(count)}.'
    elif query == 'кто все мои друзья?':
        friends_string = ', '.join(DATABASE)
        return f'Твои друзья: {friends_string}'
    elif query == 'где все мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        return f'Твои друзья в городах: {cities_string}'
    else:
        return '<неизвестный запрос>'


def process_friend(name, query):
    if name in DATABASE:
        city = DATABASE[name]
        if query == 'ты где?':
            return f'{name} в городе {city}'
        elif query == 'который час?':
            if city in UTC_OFFSET:
                time_is_now=what_time(city)
                return('Там сейчас '+time_is_now)
            else:
                return f'<не могу определить время в городе {city}>'
        else:
            return '<неизвестный запрос>'    
    else:
        return f'У тебя нет друга по имени {name}'


def process_query(query):
    elements = query.split(', ')
    if elements[0] == 'Анфиса':
        return process_anfisa(elements[1])
    else:
        return process_friend(elements[0], elements[1])


def runner():
    queries = [
        'Анфиса, сколько у меня друзей?',
        'Анфиса, кто все мои друзья?',
        'Анфиса, где все мои друзья?',
        'Анфиса, кто виноват?',
        'Коля, ты где?',
        'Соня, что делать?',
        'Антон, ты где?',
        'Алексей, который час?',
        'Артём, который час?',
        'Антон, который час?',
        'Петя, который час?'
    ]
    for query in queries:
        print(query, '-', process_query(query))

runner()