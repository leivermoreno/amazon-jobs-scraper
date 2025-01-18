from playwright.sync_api import sync_playwright
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

SP_USER = os.getenv("SPUSER")
SP_PASSWORD = os.getenv("SPPASSWORD")
TL_SID = os.getenv("TLSID")
TL_TOKEN = os.getenv("TLTOKEN")
TL_NUMBER = os.getenv("TLNUMBER")
MY_NUMBER = os.getenv("MYNUMBER")
HEADLESS = True if os.getenv("HEADLESS", "1") == "1" else False


def job():
    print("check board")
    check_jobs()
    if no_jobs:
        print("no jobs found")
        return

    print("jobs found!")
    send_call()


def check_jobs() -> None:
    global no_jobs
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=HEADLESS,
            proxy={
                "server": "https://isp.smartproxy.com:10000",
                "username": f"user-{SP_USER}-country-us",
                "password": SP_PASSWORD,
            },
        )
        context = browser.new_context(storage_state="session.json")
        page = context.new_page()
        page.goto("https://hiring.amazon.com")
        page.locator("#topSection").get_by_label("Search jobs near you").click()
        # print(page.get_by_role("heading", name="Total 1 job found").is_visible())
        page.locator('[data-test-id="filter-tag-button-distance"]').click()
        page.get_by_label("Within 30 miles").click()
        page.get_by_text("Within 50 miles").click()
        page.get_by_role("button", name="Close dialog").click()
        page.wait_for_timeout(5000)
        no_jobs = page.get_by_text("Sorry, there are no jobs").is_visible()

        # ---------------------
        context.close()
        browser.close()


def send_call():
    account_sid = TL_SID
    auth_token = TL_TOKEN
    client = Client(account_sid, auth_token)

    call = client.calls.create(
        twiml="<Response><Say>Check the board!</Say></Response>",
        to=MY_NUMBER,
        from_=TL_NUMBER,
    )

    print(call.sid)


if __name__ == "__main__":
    job()
