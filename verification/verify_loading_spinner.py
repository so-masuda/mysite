from playwright.sync_api import Page, expect, sync_playwright

def test_loading_spinner(page: Page):
  """
  This test verifies that a loading spinner appears and the button is disabled
  when the sign-in form is submitted.
  """
  # 1. Arrange: Go to the login page.
  page.goto("http://django:8000/accounts/login/")

  # 2. Act: Find the "Sign In" button and click it.
  # We don't need to fill in the form, just submit it.
  sign_in_button = page.locator('#submit-button')
  sign_in_button.click()

  # 3. Assert: Check that the button is disabled and the spinner is visible.
  expect(sign_in_button).to_be_disabled()
  spinner = sign_in_button.locator(".spinner")
  expect(spinner).to_be_visible()

  # 4. Screenshot: Capture the final result for visual verification.
  page.screenshot(path="/home/jules/verification/loading-spinner.png")

if __name__ == "__main__":
  with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    try:
      test_loading_spinner(page)
    finally:
      browser.close()
