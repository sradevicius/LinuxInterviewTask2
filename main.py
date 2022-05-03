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
    endpoint = 'https://api.github.com/search/commits?q=author:torvalds&sort=author-date&order=desc&page=1'
    auth = HTTPBasicAuth(user, token)
    response = requests.get(endpoint, auth=auth)
    return response.json()

def get_date_from_response(response):
    #date = response['data']['user']['contributionsCollection']['endedAt']
    date = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
    return date

def main():
    print(get_data(sys.argv[1], sys.argv[2])['items'][0]['commit'])


if __name__ == '__main__':
    main()
