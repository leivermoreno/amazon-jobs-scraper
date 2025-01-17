import schedule
from amazon import job
import time
from datetime import datetime
from zoneinfo import ZoneInfo


def conditional_job():
    current_hour = datetime.now(tz=ZoneInfo("America/New_York")).hour
    if 7 <= current_hour <= 21:
        job()


schedule.every(5).minutes.do(conditional_job)

while True:
    schedule.run_pending()
    time.sleep(1)
