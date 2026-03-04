import requests

urls = [
    "https://github.com/",
    "https://www.binance.com/en",
    "https://tomtit.tomsk.ru/",
    "https://jsonplaceholder.typicode.com/",
    "https://moodle.tomtit-tomsk.ru/"
]

for url in urls:
    try:
        response = requests.get(url, timeout = 5)
        code = response.status_code

        if code == 200:
            print(f"{url} - {code} - Успешно")
        elif code == 403:
            print(f"{url} - {code} - Доступ запрещен")
        elif code == 404:
            print(f"{url} - {code} - Ошибка клиента")
        elif code == 500:
            print(f"{url} - {code} - Ошибка сервера")

    except:
        print(f"{url} – Ошибка соединения")