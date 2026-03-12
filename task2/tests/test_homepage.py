from playwright.sync_api import sync_playwright

def test_homepage_load():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://selectel.ru")

        assert "Selectel" in page.title()

        browser.close()