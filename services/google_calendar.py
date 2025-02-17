from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_calendar_service():
    creds = service_account.Credentials.from_service_account_file('credentials.json', scopes=SCOPES)
    service = build('calendar', 'v3', credentials=creds)
    return service

def create_event(date):
    service = get_calendar_service()
    event = {
        'summary': 'Запись в салон красоты',
        'start': {'dateTime': date},
        'end': {'dateTime': date}
    }
    service.events().insert(calendarId='primary', body=event).execute()