import requests
import sys
from requests.auth import HTTPBasicAuth
import datetime
import time
import os


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

    while True:
        date = get_latest_push_date(username, token)
        latest_push_time = get_datetime_from_date_string(date)
        print("Print latest detected push time: ", latest_push_time)
        if latest_commit_date == None:
            latest_commit_date = latest_push_time
        if latest_commit_date != latest_push_time:
            print("Detected new push!")
            print("Last push time: ", last_commit_date)
            print("New push time: ", latest_push_time)
            if latest_mail_send_date == None or datetime.datetime.now() - datetime.timedelta(hours=24) > latest_mail_send_date:
                send_mail()
                latest_mail_send_date = datetime.datetime.now()

        print("Sleeping for 10 minutes")
        print("*"*20)
        time.sleep(600)


if __name__ == '__main__':
    #if len(sys.argv) == 3:
    #    main()
    #else:
    #    print ("This script required username and git token to be provided as command line arguments")
    try:
        username = os.environ['username']
        token = os.environ['token']
    except:
        print("Failed to get environment variables for username and github token")
    else:
        main()
