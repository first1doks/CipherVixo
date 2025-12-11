import requests

def website_info(url):
    try:
        r = requests.get(url)

        print("\n--- Информация о сайте ---")
        print("Код статуса:", r.status_code)
        print("Сервер:", r.headers.get("Server"))
        print("Content-Type:", r.headers.get("Content-Type"))
        print("Content-Length:", r.headers.get("Content-Length"))
    except:
        print("Ошибка: невозможно подключиться к сайту.")
