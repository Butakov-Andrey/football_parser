import hashlib

import requests

url = 'https://line14.bkfon-resources.com/live/currentLine/ru'
r = requests.get(url)


def get_football_ids(response):
    sports = response.json()['sports']
    football_ids = [sport['id'] for sport in sports if 'футбол' in sport['name'].lower()]
    return football_ids


def get_football_events(response, football_ids):
    events = response.json()['events']
    football_events = [event for event in events if (event['sportId'] in football_ids and event['place'] == 'live')]
    football_dict = {}
    for event in football_events:
        if "team1" in event and "team2" in event:
            unic_id = hashlib.md5(str(event['id']).encode('utf-8')).hexdigest()
            football_dict[unic_id] = f'{event["team1"]}-{event["team2"]}'
    return football_dict


def main():
    football_dict = get_football_events(r, get_football_ids(r))
    return football_dict
