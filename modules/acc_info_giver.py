import os


def get_password():
    return os.getenv("PASSWORD")


def get_username():
    return os.getenv("FORME")


def get_receiver():
    return os.getenv("FORME")


def get_api_key():
    return os.getenv("NEWSAPIKEY")

