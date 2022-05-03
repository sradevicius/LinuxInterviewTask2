import requests
import sys
from requests.auth import HTTPBasicAuth
import datetime
import time
import os
import ssl, smtplib


def send_mail(email=sender_email, receiver_email=receiver_email, password=email_password, message="New commit by Torvalds detected!"):
    port = 465
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(email, password)
        server.sendmail(email, receiver_email, message)


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
    send_mail(message="Script to detect Torvalds new commits started!")

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
        email = os.environ['email']
        email_password = os.environ['email_password']
        receiver_email = os.environ['receiver_email']
    except:
        print("Failed to get environment variables for username and github token")
    else:
        main()
