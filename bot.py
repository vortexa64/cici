import requests import random import time import os

VIDEO_URL = os.getenv("VIDEO_URL", "https://www.youtube.com/shorts/y1miCbXwHBg?vq=small")

with open("proxies.txt") as f: proxies = [line.strip() for line in f if line.strip()]

headers = { "User-Agent": "Mozilla/5.0", "Referer": "https://www.google.com/" }

def view(proxy): try: res = requests.get(VIDEO_URL, headers=headers, proxies={"http": f"http://{proxy}", "https": f"http://{proxy}"}, timeout=8) print(f"[✅] View sent with {proxy}") except: print(f"[❌] Failed with {proxy}")

while True: proxy = random.choice(proxies) view(proxy) time.sleep(15)
