import requests
from modules.acc_info_giver import get_url
from modules.mail_sender import send_mail


#make request
def news_language(language="en"):
    """language is English by default, possible languages are
    ar - arabic
    de - german
    en - english
    es - spanish
    fr - french
    he - hebrew
    it - italian
    nl - niderlandian
    no - norwegian
    pt - portuguese
    ru - russian
    sv - swedish
    ud - danish
    zh - chinese
    """
    request = requests.get(get_url()+"&language="+language)
    return request

#get dict with data
content = news_language().json()

#get articles title and description and sent emails
message = "Subject: Today's news" + "\n"
for article in content["articles"][:20]:
    if article["title"] and article["description"] is not None:
        message = message + article["title"] + "\n" + \
                  article["description"] + "\n" +\
                  article["url"] + 3 * "\n"

send_mail(message.encode('utf-8'))