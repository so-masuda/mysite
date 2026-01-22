from playwright.sync_api import Page
from playwright.sync_api import expect
from playwright.sync_api import sync_playwright


def verify_home_page(page: Page):
    """
    This test verifies that the home page loads correctly.
    """
    # 1. Arrange: Go to the home page.
    # The 'django' service is running on the Docker network,
    # so we use its name as the host.
    page.goto("http://django:8000")

    # 2. Assert: Confirm the page has the expected title.
    expect(page).to_have_title("mysite")

    # 3. Screenshot: Capture the final result for visual verification.
    page.screenshot(path="/app/verification/verification.png")


if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            verify_home_page(page)
        finally:
            browser.close()
