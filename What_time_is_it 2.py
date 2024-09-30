import datetime as dt

DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь'
}

UTC_OFFSET = {
    'Санкт-Петербург': 3,
    'Москва': 3,
    'Самара': 4,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казань': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Ростов-на-Дону': 3,
    'Уфа': 5,
    'Красноярск': 7,
    'Пермь': 5,
    'Воронеж': 3,
    'Волгоград': 3,
    'Краснодар': 3,
    'Калининград': 2
}

def what_time(friend):
    # напишите код тела функции
    # пусть она вернет время у друга из аргумента friend
    if friend in DATABASE:
        city=DATABASE[friend]
        if city in UTC_OFFSET:
            time_now=dt.datetime.utcnow()
            time1=dt.timedelta(hours=UTC_OFFSET[city])
            time2=time_now+time1
            return time2


print(what_time('Соня'))