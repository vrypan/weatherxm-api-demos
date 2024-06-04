import requests
import json
import sys
import os
from dotenv import load_dotenv
import datetime

load_dotenv()
username = os.getenv('WXM_USERNAME','')
password = os.getenv('WXM_PASSWORD','')
base_url = os.getenv('WXM_API_URL','')

station_id = sys.argv[1]

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
print('# Station = ', station_id)
today = datetime.date.today()
week_ago = today - datetime.timedelta(days=1)
r = requests.get(f'{base_url}/api/v1/me/devices/{station_id}/history?fromDate={week_ago.strftime("%Y-%m-%d")}&toDate={today.strftime("%Y-%m-%d")}', headers=headers)

for day in r.json():
  for hour in day['hourly']:
    print(hour['timestamp'], f"{hour['temperature']:.2f}")