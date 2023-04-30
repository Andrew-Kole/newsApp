import requests
from modules.mail_sender import send_mail
import datetime
import os
import typing

API_KEY: typing.Final = os.environ["API_KEY"]

def get_news(api_key, topic, date, language = "en", sortBy="publishedAt"):
    params = {"q": topic, "from": date, "sortBy": sortBy,
              "apiKey": api_key, "language": language}

    r = requests.get("https://newsapi.org/v2/everything", params=get_url())
    r.raise_for_status() 
    content = request.json()
    return content

def make_message(content):
    message = "Subject: Today's news" + "\n"
    for article in content["articles"][:20]:
      if article["title"] and article["description"] is not None:
        message = message + article["title"] + "\n" + \
                  article["description"] + "\n" +\
                  article["url"] + 3 * "\n"
    return message

def main():
    content = get_news(API_KEY, "tesla", datetime.now())
    message = make_message(content) 
    send_mail(message.encode('utf-8'))

if __name__ == "__main__":
     main()         

