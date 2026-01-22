import logging

from playwright.sync_api import sync_playwright

logger = logging.getLogger(__name__)


def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://django:8000")
    logger.info("Page content: %s", page.content())
    page.screenshot(path="verification/homepage.png")
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
