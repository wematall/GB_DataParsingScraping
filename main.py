from pprint import pprint

import  requests

# GET /users/:username/repos
host = 'https://api.github.com'
path = '/users/wematall/repos'

link = host + path

username = 'wematall'

headers = {'Accept': 'application/vnd.github.nebula-preview+json'}

response = requests.get(link, headers=headers)

data = response.json()

with open('user_repos.json', 'wb') as file:
    file.write(response.content)

# pprint(data)

for item in data:
    print("User repositories: " + item['name'])