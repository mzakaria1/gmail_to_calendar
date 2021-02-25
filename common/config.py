
                        #---------------- GMAIL VARIABLES ---------------

# GMAIL API VARIABLES
MARK_AS_READ = {'removeLabelIds': ['UNREAD']}
NO_UNREAD_LEAVE_MAIL_FOUND = "No UnRead Email Found for Employee Leave"
EMAIL_FROM = "Wajahat Chaudhry <wajahat@eurustechnologies.com>"


# GMAIL AUTH VARIABLES
GMAIL_SCOPES = ["https://www.googleapis.com/auth/gmail.modify"]
GMAIL_TOKEN_PICKLE = "token.pickle"
GMAIL_CRED_FILE_PATH = "/gmail/credentials.json"
GMAIL_API_NAME = "gmail"
GMAIL_API_VERSION = "v1"


                                #---------------- CALENDAR VARIABLES ---------------

# CALENDAR API VARIABLES
CALENDAR_NAME = "Employee Leaves"
TIME_ZONE = 'Asia/Karachi'
CALENDAR = {
    'summary': CALENDAR_NAME,
    'timeZone': TIME_ZONE,
}


# CALENDAR AUTH VARIABLES
DATE_MATCH_PATTERN = '\d{4}\-\d{2}\-\d{2}\s\s'
CALENDAR_SCOPES = ['https://www.googleapis.com/auth/calendar']
CALENDAR_TOKEN_PICKLE = "token.pickle1"
CALENDAR_CRED_FILE_PATH = "/calender/calender.json"
CALENDAR_API_NAME = "calendar"
CALENDAR_API_VERSION = "v3"
