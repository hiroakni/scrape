import time
import requests

def main(message, token):
    time.sleep(10)
    line_notify_token = token
    line_notify_api = 'https://notify-api.line.me/api/notify'
    payload = {'message': '\n' + message }
    headers = {'Authorization': 'Bearer ' + line_notify_token}
    try:        
        line_notify = requests.post(line_notify_api, data=payload, headers=headers)
        if line_notify.status_code == 200:
            print("success sent message")
    except Exception as e:
        print("line notify exception")
        print(e)
        pass
    time.sleep(1)