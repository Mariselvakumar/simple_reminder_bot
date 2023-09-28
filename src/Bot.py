from src.desktop_notification import notify
from datetime import datetime
from datetime import timedelta
import time


def time_formatter(non_formatted_timestamp):
    return str(non_formatted_timestamp).split('.')[0].split(' ')[1]


def get_seconds(ti):
    time_frame = [3600, 60, 1]
    time_splits = str(ti).split(':')
    seconds = 0
    for index in range(0, 3, 1):
        seconds = seconds + int(time_splits[index]) * time_frame[index]
    return seconds


def current_time_seconds():
    ti = time_formatter(datetime.now())
    return get_seconds(ti)


def get_fake_reminder(buffer):
    ti = time_formatter(datetime.now() + timedelta(0, buffer))
    return ti


def trigger_bot(reminder_time, title, message):
    rt = get_seconds(reminder_time)
    ct = current_time_seconds()
    if ct < rt:
        time.sleep(rt - ct)
        notify(title, message)
