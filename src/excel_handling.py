from src.Bot import get_fake_reminder
import pandas as pd


def read_excel():
    try:
        data_frame, excel_data = pd.read_excel('resources/schedules.xlsx'), dict()
        for column_name in data_frame.columns:
            excel_data[column_name] = list(data_frame[column_name])
        times = excel_data['Time']
        titles = excel_data['Header']
        messages = excel_data['Message']
        return times, titles, messages
    except FileNotFoundError:
        print('file not found')


def fake_excel_data():
    times = [get_fake_reminder(5), get_fake_reminder(10), get_fake_reminder(15)]
    titles = ['Task 1', 'Task 2', 'Task 3']
    messages = ['Task 1: Messages', 'Task 2: Messages', 'Task 3: Messages']
    return times, titles, messages

