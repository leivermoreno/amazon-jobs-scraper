FROM python:3.12.3

WORKDIR /home/app

ENV PYTHONUNBUFFERED=1

COPY requirements.txt requirements.txt

RUN apt-get update && \
    pip install --no-cache-dir -r requirements.txt && \
    playwright install-deps && playwright install chromium

COPY . .

CMD [ "python", "job.py"]