import requests
import sys
from requests.auth import HTTPBasicAuth
import datetime

def send_mail():
    pass

def get_datetime_from_date_string(date):
    date = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
    return date

def main():
    latest_mail_send_date = None
    latest_commit_date = None

    date = get_latest_push_date(sys.argv[1], sys.argv[2])
    date = get_datetime_from_date_string(date)
    print(date)
    ## Some dates returned are far in the future, i.e. 2099 or 2038
    ## I also don't really care about commits done before 2022, so the below code
    ## Should get rid of those future commits in response
    pass


if __name__ == '__main__':
    if len(sys.argv) == 3:
        main()
    else:
        print ("This script required username and git token to be provided as command line arguments")
