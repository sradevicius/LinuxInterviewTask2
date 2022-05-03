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

def get_date_from_response(response):
    #date = response['data']['user']['contributionsCollection']['endedAt']
    date = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
    return date

def main():
    data = get_data(sys.argv[1], sys.argv[2])
    last_commit_date = data['items'][0]['commit']['author']['date']
    print(last_commit_date)


if __name__ == '__main__':
    main()
