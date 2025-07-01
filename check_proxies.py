import requests

url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=1000&country=all&ssl=all&anonymity=elite"
res = requests.get(url)
proxies = res.text.strip().split('\n')[:50]  # Ambil 50 proxy

with open("proxies.txt", "w") as f:
    for proxy in proxies:
        f.write(proxy + "\n")

print(f"Saved {len(proxies)} proxies.")
