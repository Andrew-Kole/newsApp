import requests
from modules.acc_info_giver import get_url
from modules.mail_sender import send_mail

#make request
request = requests.get(get_url())

#get dict with data
content = request.json()

#get articles title and description and sent emails
message = ""
for article in content["articles"]:
    if article["title"] and article["description"] is not None:
        message = message + article["title"] + "\n" + article["description"] + "\n"*3

send_mail(message.encode('utf-8'))