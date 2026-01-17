from playwright.sync_api import Page
from playwright.sync_api import expect
from playwright.sync_api import sync_playwright


def verify_homepage(page: Page):
    """
    This test verifies that the homepage loads correctly.
    """
    # 1. Arrange: Go to the homepage.
    page.goto("http://django:8000")

    # 2. Assert: Confirm the page title is correct.
    expect(page).to_have_title("mysite")

    # 3. Screenshot: Capture the final result for visual verification.
    page.screenshot(path="verification/verification.png")


if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            verify_homepage(page)
        finally:
            browser.close()
