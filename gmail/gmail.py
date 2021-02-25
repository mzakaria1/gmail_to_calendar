import json
import base64
import re
from datetime import datetime
from common.config import (
    MARK_AS_READ,
    EMAIL_FROM,
    DATE_MATCH_PATTERN,
    NO_UNREAD_LEAVE_MAIL_FOUND,
    GMAIL_SCOPES,
    GMAIL_TOKEN_PICKLE, 
    GMAIL_CRED_FILE_PATH,
    GMAIL_API_NAME,
    GMAIL_API_VERSION
)
from common.auth import authenticate
from pprint import pprint


def get_leave_info():

    service = authenticate(GMAIL_TOKEN_PICKLE, GMAIL_CRED_FILE_PATH, GMAIL_SCOPES, GMAIL_API_NAME, GMAIL_API_VERSION)

    return get_applied_leave_info(service)



def get_applied_leave_info(service, user_id='me'):
    response = {}
    all_messages = service.users().messages().list(userId=user_id).execute().get('messages',[])
    for messages in all_messages:
        message = service.users().messages().get(userId=user_id, id=messages['id']).execute()
        # pprint(message)
        UNREAD = message['labelIds'][0]
        if UNREAD == 'UNREAD':
            payload = message['payload']
            for header in payload['headers']:
                if header['name'] == 'From' and header['value'] == EMAIL_FROM:
                    part = payload['parts'][0]
                    encoded_part = part.get('body').get('data')
                    decoded_msg_body_data = base64.urlsafe_b64decode(encoded_part.encode('ASCII')).decode('utf-8')
                    print(decoded_msg_body_data)

                    name = decoded_msg_body_data.split(" has applied")
                    name = name[0].splitlines()
                    name = name[-1]

                    dates = re.findall(DATE_MATCH_PATTERN, decoded_msg_body_data)
                    # Marking As Read 
                    mark_as_read(service, message)
                    
                    response[name] = dates
    if not bool(response):
        response[NO_UNREAD_LEAVE_MAIL_FOUND] = []
        return response
    else:
        return response


def mark_as_read(service, message,user_id='me'):
    marked_read = service.users().messages().modify(userId=user_id, id=message['id'], body=MARK_AS_READ).execute()
    if marked_read:
        print("Email has been successfully Marked AS Read!")

