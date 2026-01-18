
from playwright.sync_api import Page, expect, sync_playwright

def verify_homepage(page: Page):
    """
    This test verifies that the homepage renders correctly after bundling Bootstrap.
    """
    # 1. Arrange: Go to the homepage.
    # The Django service is running on port 8000 and is aliased as 'django' in the Docker network.
    page.goto("http://django:8000")

    # 2. Assert: Confirm the page title is correct.
    expect(page).to_have_title("mysite")

    # 3. Assert: Check for a key Bootstrap element to ensure CSS is applied.
    # We'll check for the visibility of the main navbar.
    navbar = page.get_by_role("navigation")
    expect(navbar).to_be_visible()

    # 4. Screenshot: Capture the final result for visual verification.
    page.screenshot(path="verification/homepage.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            verify_homepage(page)
        finally:
            browser.close()
