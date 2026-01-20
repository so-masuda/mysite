from playwright.sync_api import Page
from playwright.sync_api import expect
from playwright.sync_api import sync_playwright


def run(page: Page):
    page.goto("http://django:8000/accounts/signup/")
    expect(page.get_by_role("heading", name="Sign Up")).to_be_visible()
    page.screenshot(path="verification/screenshot.png")


with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    run(page)
    browser.close()
