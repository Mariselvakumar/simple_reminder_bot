import src.excel_handling
from src.Bot import trigger_bot
from src.desktop_notification import notify


#schedule_times, schedule_titles, schedule_messages = src.excel_handling.fake_excel_data()
schedule_times, schedule_titles, schedule_messages = src.excel_handling.read_excel()
for x in range(len(schedule_times)):
    trigger_bot(schedule_times[x], schedule_titles[x], schedule_messages[x])
else:
    notify('End Of Day', 'There are no tasks for today, HAVE FUN!!!')

