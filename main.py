import time
import requests

url = "https://youtube.com/shorts/y1miCbXwHBg?si=Kkp1d2d7IjSzmuJ0"  # ganti linkmu di sini

while True:
    print("Nonton video...")
    requests.get(url)
    time.sleep(60)
