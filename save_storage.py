import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://hiring.amazon.com/#/")
    page.locator('[data-test-id="consentBtn"]').click()
    page.get_by_role("button").first.click()
    page.locator("#topSection").get_by_label("Search jobs near you").click()
    page.get_by_label("Guided Search").get_by_placeholder(
        "Enter zipcode or city"
    ).click()
    page.get_by_label("Guided Search").get_by_placeholder("Enter zipcode or city").fill(
        "33178"
    )
    page.get_by_text("33178").click()
    page.wait_for_timeout(3000)
    page.get_by_role("button", name="Next").click()
    page.get_by_role("button", name="Next").click()
    page.get_by_role("button", name="Skip").click()
    page.get_by_role("button", name="Skip").click()
    page.get_by_role("button", name="Done").click()
    page.locator('[data-test-id="filter-tag-button-distance"]').click()
    page.get_by_label("Within 30 miles").click()
    page.get_by_text("Within 50 miles").click()
    page.get_by_role("button", name="Close dialog").click()
    page.wait_for_timeout(3000)

    # ---------------------
    context.storage_state(path="session.json")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
