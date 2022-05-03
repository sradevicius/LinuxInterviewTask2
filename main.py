import requests
import sys
from requests.auth import HTTPBasicAuth
import datetime

#def get_data(user, passwd):
#    auth = HTTPBasicAuth(user, passwd)
#    endpoint = 'https://api.github.com/graphql'
#    query = """query {
#      user(login: "torvalds"){
#        contributionsCollection {
#          endedAt
#        }
#      }
#    }
#    """
#
#    response = requests.post(endpoint, json={"query": query}, auth=auth)
#    return response.json()

def get_data(user, token):
    """Returns latest commits by Torvalds sorted by date. Two major notes, one is that github only 
    indexes master branch, other is that some commits are in the far future"""
    endpoint = 'https://api.github.com/search/commits?q=author:torvalds&sort=author-date&order=desc&page=1'
    auth = HTTPBasicAuth(user, token)
    response = requests.get(endpoint, auth=auth)
    return response.json()

def get_datetime_from_date_string(date):
    #date = response['data']['user']['contributionsCollection']['endedAt']
    #date = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
    date = datetime.datetime.strptime(date[:-10], '%Y-%m-%dT%H:%M:%S')
    return date

def main():
    data = get_data(sys.argv[1], sys.argv[2])
    ## Some dates returned are far in the future, i.e. 2099 or 2038
    ## I also don't really care about commits done before 2022, so the below code
    ## Should get rid of those future commits in response
    for i in range(len(data['items'])):
        last_commit_date = data['items'][i]['commit']['author']['date']
        if last_commit_date[:4] == '2022':
            break
    last_commit_date = get_datetime_from_date_string(last_commit_date)
    print(last_commit_date)



if __name__ == '__main__':
    if len(sys.argv) == 3:
        main()
    else:
        print ("This script required username and git token to be provided as command line arguments")
