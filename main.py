import requests
import os

api_key = os.getenv("NEWSAPIKEY")

url = f"https://newsapi.org/v2/everything?q=tesla&from=2023-03-29" \
      "&sortBy=publishedAt&apiKey=" \
      f"{api_key}"

#make request
request = requests.get(url)

#get dict with data
content = request.json()

#get articles title and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])