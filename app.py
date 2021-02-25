from gmail.gmail import get_leave_info
from calender.calender import create_calender_event, get_calendar_colors
from pprint import pprint

from common.config import NO_UNREAD_LEAVE_MAIL_FOUND

def get_applied_leave_detail_gmail():
    response = get_leave_info()
    pprint(response)

    if NO_UNREAD_LEAVE_MAIL_FOUND in response.keys():
        print(NO_UNREAD_LEAVE_MAIL_FOUND)
    else:
        for name, dates in response.items():
            for date in dates:
                print("Date: ", date)
            add_event_into_Calendar(dates, name)


def add_event_into_Calendar(dates, name):
    create_calender_event(dates, name)


if __name__ == '__main__':
    try:
        get_applied_leave_detail_gmail()
    except Exception as ex:
        print(":::You Get Exception::: {}".format(ex))