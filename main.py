import requests
from modules.acc_info_giver import get_url
from modules.mail_sender import send_mail


#make request
def news_language(command="&language=", language="en"):
    request = requests.get(get_url()+command+language)
    return request

#get dict with data
content = news_language().json()

#get articles title and description and sent emails
message = ""
for article in content["articles"]:
    if article["title"] and article["description"] is not None:
        message = message + article["title"] + "\n" + \
                  article["description"] + "\n" +\
                  article["url"] + 3 * "\n"

send_mail(message.encode('utf-8'))