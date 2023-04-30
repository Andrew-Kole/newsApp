import requests
from modules.acc_info_giver import get_api_key
from modules.mail_sender import send_mail

def get_url(api_key=get_api_key(), topic = "tesla", language = "en"):
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

        Topic is tesla by default, but you can choose other topic
        """
    url = f"https://newsapi.org/v2/everything?q={topic}&from=2023-03-29" \
          "&sortBy=publishedAt&apiKey=" \
          f"{api_key}&language={language}"
    return url
#make request
request = requests.get(get_url())


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