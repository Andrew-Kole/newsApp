import os


def get_password():
    return os.getenv("PASSWORD")


def get_username():
    return os.getenv("FORME")


def get_receiver():
    return os.getenv("FORME")


def get_api_key():
    return os.getenv("NEWSAPIKEY")


def get_url(api_key=get_api_key()):
    url = f"https://newsapi.org/v2/everything?q=tesla&from=2023-03-29" \
          "&sortBy=publishedAt&apiKey=" \
          f"{api_key}"
    return url
