from playwright.sync_api import sync_playwright
import time

URL = "https://pro.jornada.com.pe/ediciones"
OUTPUT_FILE = "links.txt"
MAX_PAGES = 60
DELAY = 3

links = []
seen = set()

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False,
        proxy={"server": "socks5://127.0.0.1:9150"}
    )

    context = browser.new_context()
    page = context.new_page()

    def handle_response(response):
        url = response.url
        if "/files/large/" in url:
            if url not in seen:
                seen.add(url)
                links.append(url)
                print(f"🔗 Capturado {len(links)}")

    page.on("response", handle_response)

    print("🌐 Abriendo visor...")
    page.goto(URL, timeout=60000)
    time.sleep(6)

    for _ in range(MAX_PAGES):
        page.keyboard.press("ArrowRight")
        time.sleep(DELAY)

    browser.close()

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for link in links:
        f.write(link + "\n")

print(f"\n✅ {len(links)} links guardados en {OUTPUT_FILE}")
