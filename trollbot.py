# Подключите библиотеку random и дайте ей краткое имя
import random as r
answers = ['Лучше всех :)', 'Отличненько!', 'Ничего, жить буду','Пока не родила!','Не жалуюсь']

def how_are_you():
    answer=r.choice(answers)
    return answer

print(how_are_you())