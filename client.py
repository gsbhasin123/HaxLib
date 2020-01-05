import requests

api = 'https://discordapp.com/api/v6'

class client(object):
    def __init__(self, token):
        self.token = token
    def send_msg(self, channel_id, msg:str):
        url = api + f'/channels/{channel_id}/messages'
        payload = {
          "content": msg,
          "tts": 'false',
           "embed": {
            "title": "Hello, Embed!",
            "description": "This is an embedded message."
            }
          }
        headers = {
          "Authorization":f"Bot {self.token}"
          }
        r = requests.post(url=url, headers=headers, json=payload)
        print(r.text)