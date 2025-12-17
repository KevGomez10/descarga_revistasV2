import requests
import os
import time
import random

INPUT_FILE = "links.txt"
OUTPUT_FOLDER = "diario"

proxies = {
    "http": "socks5h://127.0.0.1:9150",
    "https": "socks5h://127.0.0.1:9150",
}

headers = {
    "User-Agent": "Mozilla/5.0"
}

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    links = [line.strip() for line in f if line.strip()]

session = requests.Session()
session.proxies.update(proxies)
session.headers.update(headers)

for i, url in enumerate(links, start=1):
    try:
        print(f"⬇️ Descargando {i}/{len(links)}")
        r = session.get(url, timeout=30)
        r.raise_for_status()

        with open(f"{OUTPUT_FOLDER}/{i}.jpg", "wb") as f:
            f.write(r.content)

        time.sleep(random.uniform(1.5, 3.5))

    except Exception as e:
        print(f"❌ Error en página {i}: {e}")
