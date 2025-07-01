import requests
import random
import time
import os

VIDEO_URL = os.environ.get("VIDEO_URL") or "https://youtube.com/shorts/y1miCbXwHBg"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Referer": "https://www.google.com/",
}

def view(proxy):
    try:
        res = requests.get(
            VIDEO_URL,
            headers=headers,
            proxies={
                "http": f"http://{proxy}",
                "https": f"http://{proxy}"
            },
            timeout=8
        )
        print(f"[✅] View sent with {proxy}")
    except:
        print(f"[❌] Failed with {proxy}")

with open("proxies.txt") as f:
    proxies = f.read().splitlines()

for i in range(10):  # Kirim 10 view
    proxy = random.choice(proxies)
    view(proxy)
    time.sleep(2)
