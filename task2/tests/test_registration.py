from playwright.sync_api import sync_playwright

def test_registration_button():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://selectel.ru")

        with context.expect_page() as new_page_info:
            page.get_by_role("link", name="Создать аккаунт").first.click()

        new_page = new_page_info.value

        assert "registration" in new_page.url

        browser.close()