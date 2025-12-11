import requests

def ip_lookup(ip):
    try:
        url = f"http://ip-api.com/json/{ip}"
        r = requests.get(url).json()

        print("\n--- Информация об IP ---")
        print("Страна:", r.get("country"))
        print("Регион:", r.get("regionName"))
        print("Город:", r.get("city"))
        print("Провайдер:", r.get("isp"))
        print("Часовой пояс:", r.get("timezone"))
    except:
        print("Произошла ошибка.")
