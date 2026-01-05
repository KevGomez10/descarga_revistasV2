from playwright.sync_api import sync_playwright
import time

URL = "https://www.zinio.com/mx/publications/vogue-latin-america/1640"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    def handle_response(response):
        url = response.url
        if any(ext in url for ext in [".jpg", ".jpeg", ".png", ".webp"]):
            print("🖼 Imagen detectada:", url)

    page.on("response", handle_response)

    print("🌐 Abriendo visor…")
    page.goto(URL)

    time.sleep(25)

    browser.close()
