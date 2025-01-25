import schedule
from amazon import job
import time
from datetime import datetime
from zoneinfo import ZoneInfo
import os


JOB_INTERVAL = int(os.getenv("JOB_INTERVAL"))


def conditional_job():
    current_hour = datetime.now(tz=ZoneInfo("America/New_York")).hour
    if 7 <= current_hour <= 21:
        job()


def retry_job():
    while True:
        try:
            job()
            break
        except Exception as e:
            print(f"Job failed: {e}")


schedule.every(JOB_INTERVAL).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
