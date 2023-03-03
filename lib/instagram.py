from pathlib import Path
from random import choice

from instagrapi import Client
from instagrapi.exceptions import LoginRequired
from instagrapi.types import Comment

SETTINGS = Path("session.json")


def create_logged_in_client(account: str, password: str) -> Client:
    api = Client()
    if SETTINGS.exists():
        api.load_settings(SETTINGS)
    api.login(account, password)
    try:
        api.get_timeline_feed()
    except LoginRequired:
        # delete current settings and restart
        SETTINGS.unlink()
        return create_logged_in_client(account, password)
    api.dump_settings(SETTINGS)
    return api


def get_comments_from_url(api: Client, url: str) -> list[Comment]:
    key = api.media_pk_from_url(url)
    return api.media_comments(key)


def pick_random_comment_from_url(api: Client, url: str) -> Comment:
    return choice(get_comments_from_url(api, url))
