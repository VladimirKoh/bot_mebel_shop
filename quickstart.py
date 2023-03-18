import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


CREDENTIALS_FILE = 'creds.json'
spreadsheet_id = '1h54yqNZXx-P8DR4ocoNb0K-i5FLYnQqsuk4-VmiCPIM'

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = build('sheets', 'v4', http = httpAuth)



range_ = 'Лист1!A1'  # TODO: Update placeholder value.

# How the input data should be interpreted.
value_input_option = 'RAW'  # TODO: Update placeholder value.

# How the input data should be inserted.
value_range_body = {
    'values': [['pidr', '86363463636']]
}

values = service.spreadsheets().values().append(spreadsheetId=spreadsheet_id, 
                                                range=range_, 
                                                valueInputOption=value_input_option, 
                                                body=value_range_body).execute()