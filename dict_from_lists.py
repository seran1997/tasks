# Задача 1
# Научите Анфису собирать словарь friends из двух списков. 
# В коде приготовлены два списка: 
# friends_names, имена друзей;
# friends_cities — города, где живут друзья.
# Списки соответствуют друг другу: friends_names[0] живёт в городе friends_cities[0].
# Заполните элементами словарь friends (он уже объявлен в коде). Ключом каждого элемента должно быть имя друга, значением — город, в котором он живёт.
# Для этого в цикле создайте элементы словаря из элементов списков с одинаковыми индексами.
# Для проверки напечатайте на экран сообщение "Лена живёт в городе <город>", используя доступ по нужному ключу в словаре friends.


friends_names = ['Аня', 'Коля', 'Лёша', 'Лена', 'Миша']
friends_cities = ['Владивосток', 'Красноярск', 'Москва', 'Обнинск', 'Чебоксары']

# Объявлен пустой словарь, его нужно будет наполнить элементами, 
# каждый из которых составлен по схеме "имя: город"
friends =  {}

# Допишите ваш код сюда
for i in range(0, len(friends_names)):
    friends[friends_names[i]]=friends_cities[i]

print("Лена живёт в городе", friends['Лена'])