
from __future__ import print_function
import datetime
import os
import csv
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar']


def get_service():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('calendar', 'v3', credentials=creds)


def load_birthdays(filepath):
    birthdays = []
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['Name']
            md = row['MM-DD']
            birthdays.append((name, md))
    return birthdays


def load_emails(filepath):
    emails = []
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:
                emails.append(row[0])
    return emails


def create_calendar(service):
    calendar = {
        'summary': 'Family Birthdays',
        'timeZone': 'Europe/Warsaw'
    }
    created_calendar = service.calendars().insert(body=calendar).execute()
    print(f"✔️ Created calendar: {created_calendar['summary']} (ID: {created_calendar['id']})")
    return created_calendar['id']


def create_birthday_events(service, calendar_id, birthdays, emails):
    for name, md in birthdays:
        event = {
            'summary': f'Birthday: {name}',
            'start': {
                'dateTime': f'2025-{md}T09:00:00',
                'timeZone': 'Europe/Warsaw',
            },
            'end': {
                'dateTime': f'2025-{md}T10:00:00',
                'timeZone': 'Europe/Warsaw',
            },
            'recurrence': [
                'RRULE:FREQ=YEARLY'
            ],
            'attendees': [{'email': email} for email in emails],
            'reminders': {
                'useDefault': True,
            },
        }
        service.events().insert(calendarId=calendar_id, body=event, sendUpdates='all').execute()
        print(f"➕ Created event for {name}")


if __name__ == '__main__':
    service = get_service()
    birthdays = load_birthdays('birthdays.csv')
    emails = load_emails('emails.csv')
    calendar_id = create_calendar(service)
    create_birthday_events(service, calendar_id, birthdays, emails)
