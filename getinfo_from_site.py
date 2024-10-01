# Откройте в браузере новый URL с параметрами: страницу http://wttr.in/?0T. Посмотрите, что получается.
# Затем сделайте аналогичный HTTP-запрос на чистом Python.
import requests

url = 'http://wttr.in/?0T'

response = requests.get(url)  # выполните HTTP-запрос

print(response.text)  # напечатайте текст HTTP-ответа