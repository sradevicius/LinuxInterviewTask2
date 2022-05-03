import requests
import sys
from requests.auth import HTTPBasicAuth
import datetime


def send_mail():
    pass


def get_latest_push_date(user, token):
    auth = HTTPBasicAuth(user, token)
    endpoint = 'https://api.github.com/users/torvalds/events/public'
    response = requests.get(endpoint, auth=auth)
    for i in range(len(response.json())):
        if response.json()[i]['type'] == 'PushEvent':
            return response.json()[i]['created_at']


def get_datetime_from_date_string(date):
    date = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
    return date

def main():
    latest_mail_send_date = None
    latest_commit_date = None

    date = get_latest_push_date(sys.argv[1], sys.argv[2])
    print(date)
    pass


if __name__ == '__main__':
    if len(sys.argv) == 3:
        main()
    else:
        print ("This script required username and git token to be provided as command line arguments")
