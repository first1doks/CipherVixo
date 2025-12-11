import requests

PLATFORMS = {
    "GitHub": "https://github.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "TikTok": "https://www.tiktok.com/@{}",
}

def username_search(username):
    print("\n--- Поиск пользователя ---")
    for name, url in PLATFORMS.items():
        profile = url.format(username)
        r = requests.get(profile)
        if r.status_code == 200:
            print(f"[+] {name}: найден → {profile}")
        else:
            print(f"[-] {name}: не найден")
