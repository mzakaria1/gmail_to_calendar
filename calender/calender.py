from common.config import (
    CALENDAR_NAME,
    CALENDAR,
    CALENDAR_SCOPES,
    TIME_ZONE,
    CALENDAR_SCOPES,
    CALENDAR_TOKEN_PICKLE, 
    CALENDAR_CRED_FILE_PATH,
    CALENDAR_API_NAME,
    CALENDAR_API_VERSION
)

from common.auth import authenticate

from pprint import pprint
import random


def create_calender_event(dates, name):

    service = authenticate(CALENDAR_TOKEN_PICKLE, CALENDAR_CRED_FILE_PATH, CALENDAR_SCOPES, CALENDAR_API_NAME, CALENDAR_API_VERSION)

    # # Code
    time = dates[0].split("  ")
    start_date = time[0]
    end_date = time[0]

    for x in range(len(dates)):
        time = dates[x].split("  ")
        start_date = time[0]
        end_date = time[0]
        create_event(service, name, start_date, end_date)


def create_event(service, name, start_date, end_date):
    colors = service.colors().get().execute()

    is_calendar_name_exist = False
    calendar_list_names={}
    page_token = None

    while True:
        calendar_list = service.calendarList().list(pageToken=page_token).execute()
        for calendar_list_entry in calendar_list['items']:
            calendar_list_names[calendar_list_entry['summary']] = calendar_list_entry['id']

        page_token = calendar_list.get('nextPageToken')
        if not page_token:
            break

    if CALENDAR_NAME not in calendar_list_names.keys():
        created_calendar = service.calendars().insert(body=CALENDAR).execute()
        calendar_list_names[created_calendar['summary']] = created_calendar['id']

    name = name + " Applied Leave"
    event_request_body ={
        'summary': name,
        'start':{
            'date': start_date,
            'timeZone': TIME_ZONE
        },
        'end':{
            'date': end_date,
            'timeZone': TIME_ZONE
        },
        'colorId': get_calendar_colors(service),
        'visibility': 'default',
        'reminders':{
            'useDefault':True,
        },
    }

    response = service.events().insert(calendarId=calendar_list_names[CALENDAR_NAME], body=event_request_body).execute()
    print(name," Event of DateTime",start_date," has been created Successfully.")


def get_calendar_colors(service, userId='me'):
    colors = service.colors().get().execute()

    event_colors = colors['event']
    event_color_ids_list = [int(i) for i in event_colors.keys()] 
    event_color_id = random.choice(event_color_ids_list)
    return event_color_id
