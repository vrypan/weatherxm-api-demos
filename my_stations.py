import requests
import json
import sys
import os
from dotenv import load_dotenv

load_dotenv()
username = os.getenv('WXM_USERNAME','')
password = os.getenv('WXM_PASSWORD','')
base_url = os.getenv('WXM_API_URL','')

if username == '' or password == '' or base_url == '':
  print('Missing username/password')
  sys.exit(1)

headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json'
  }

payload = {'username': username, 'password':password}
r = requests.post(f'{base_url}/api/v1/auth/login', data=json.dumps(payload), headers=headers)

if r.status_code == requests.codes.ok:
  auth_token = r.json()['token']
else:
  print(r.text)
  sys.exit(1)

headers['Authorization'] = f'Bearer {auth_token}'

r = requests.get(f'{base_url}/api/v1/me/devices', headers=headers)
if not r.status_code == requests.codes.ok:
  print(r.text)
  sys.exit(1)

for station in r.json():
  print('='*50)
  print('Station ID: ' + station['id'])
  print('Station Name: ' + station['name'])
  print('Current Weather:')
  for w in station['current_weather']:
    print(f'\t{w}\t{station['current_weather'][w]}')

