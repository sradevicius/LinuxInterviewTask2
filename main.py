import requests
import sys
from requests.auth import HTTPBasicAuth

def get_data(user, passwd):
    auth = HTTPBasicAuth(user, passwd)
    endpoint = 'https://api.github.com/graphql'
    query = """query {
      user(login: "torvalds"){
        contributionsCollection {
          endedAt
        }
      }
    }
    """

    response = requests.post(endpoint, json={"query": query}, auth=auth)
    return response

def main():
    pass


