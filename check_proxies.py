import requests

url = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=5000&country=all&ssl=all&anonymity=all'

res = requests.get(url) proxies = res.text.strip().split('\n')[:50]

working = []

for proxy in proxies: try: r = requests.get('https://httpbin.org/ip', proxies={"http": f"http://{proxy}", "https": f"http://{proxy}"}, timeout=5) print(f"✅ {proxy}") working.append(proxy) except: print(f"❌ {proxy}")

with open('proxies.txt', 'w') as f: f.write('\n'.join(working))

print(f"[🔥] {len(working)} proxy aktif disimpan ke proxies.txt")
