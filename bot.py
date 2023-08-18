import re
import time
import pytchat
import requests

bot_token = '1049651177:AAHJjJYcDFIKI0YfeMypwglXdwataibyTko'
chat_id = '792219547'

yt_url = input("Enter Youtube Live Link: ")
yt_id = yt_url.split("=")[-1]

def GrabURL(string):
    urls = re.findall('(https?|ftp):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])', string)
    for url in urls:
        full_url = f"{url[0]}://{url[1]}{url[2]}"
        burl = f'https://api.telegram.org/bot{bot_token}/sendMessage'
        data = {
            'chat_id': chat_id,
            'text': full_url
        }

        response = requests.post(burl, data=data)
        print(response.text)
        print(full_url)

chat = pytchat.create(video_id=yt_id)
while chat.is_alive():
    for c in chat.get().sync_items():
        try:
            if c.author.name and c.message:
                print(f"{c.datetime} [{c.author.name.encode('utf-8').decode()}]  {c.message.encode('utf-8').decode()}")
        except Exception as e:
            print("An error occurred:", e)