import requests

from pprint import pprint

host = 'https://www.googleapis.com'
# path = '/youtube/v3/channels'
path = '/youtube/v3/search'

API_KEY_HERE = 'AIzaSyCZUEQVvFYT1OmJDDmJiTyMSEgLz6F-vOE'

link = host + path

headers = {'Accept': 'application/json'}

params = {'channelId': 'UCBbeDje34deoh6ELVL9seAg',
          'part': 'snippet',
          'maxResults': 50,
          'key': API_KEY_HERE}

response = requests.get(link, headers=headers, params=params)

data = response.json()

with open('channel_content.json', 'wb') as file:
   file.write(response.content)

pprint(data)

