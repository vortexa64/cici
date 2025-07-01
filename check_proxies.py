import requests

url = "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt"
res = requests.get(url)
proxies = res.text.strip().split('\n')[:50]  # Ambil 50 proxy

with open("proxies.txt", "w") as f:
    for proxy in proxies:
        f.write(proxy + "\n")

print(f"Saved {len(proxies)} proxies.")
