def get_together_games(a,b):
    a1=set(a)
    b1=set(b)
    c=a1.intersection(b1)
    return c

anfisa_games = [
    'Online-chess',
    'Города',
    'DOOM',
    'Крестики-нолики'
]
alisa_games = [
    'DOOM',
    'Online-chess',
    'Города',
    'GTA',
    'World of tanks'
]
# Вызовите функцию со списками игр в качестве параметров
together_games = get_together_games(anfisa_games,alisa_games)
# Напечатайте итоговый перечень игр в цикле
for game in together_games:
    print('👾',game )