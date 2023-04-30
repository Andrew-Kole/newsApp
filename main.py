import requests
from modules.acc_info_giver import get_api_key
from modules.mail_sender import send_mail
import datetime

def get_url(api_key=get_api_key(), topic = "tesla", language = "en",
            date=datetime.date.today().isoformat(), sortBy="publishedAt" ):
    """language is English by default, possible languages are
        ar - arabic
        de - german
        en - englishdatetime.date.today().isoformat()
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

        Topic is tesla by default, but you can choose other topic
        """
    params = {"q": topic, "from": date, "sortBy": sortBy,
              "apiKey": api_key, "language": language}
    return params
#make request
request = requests.get("https://newsapi.org/v2/everything", params=get_url())

#get dict with data
content = request.json()

#get articles title and description and sent emails
message = "Subject: Today's news" + "\n"
for article in content["articles"][:20]:
    if article["title"] and article["description"] is not None:
        message = message + article["title"] + "\n" + \
                  article["description"] + "\n" +\
                  article["url"] + 3 * "\n"

send_mail(message.encode('utf-8'))