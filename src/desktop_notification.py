from notifypy import Notify as notify_config
from pathlib import Path


def notify(title, message):
    notification = notify_config(
        default_notification_title=title,
        default_notification_message=message,
        default_notification_icon=str(Path(__file__).parent.parent) + '/resources/bot.ico',
        default_notification_application_name='Reminder Bot'
    )
    notification.send()
