from playwright.sync_api import sync_playwright


def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    # The django service is running on port 8000 inside the docker network
    # The service name is 'django', so we use that as the hostname.
    page.goto("http://django:8000")
    page.screenshot(path="verification/homepage.png")
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
