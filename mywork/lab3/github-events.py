#!/usr/bin/env python3
import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
if not GHUSER:
    print("Error: GITHUB_USER environment variable not set.")
    exit(1)

url = f'https://api.github.com/users/{GHUSER}/events'
r = json.loads(requests.get(url).text)

for x in r[:5]:
    event = x['type'] + ' :: ' + x['repo']['name']
    print(event)
