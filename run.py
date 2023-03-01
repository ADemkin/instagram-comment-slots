from pathlib import Path
from random import choice
import os
import sys

from dotenv import load_dotenv
from instagrapi import Client
from instagrapi.exceptions import LoginRequired
from instagrapi.types import Comment


SETTINGS = Path('session.json')


def create_logged_in_client() -> Client:
    api = Client()
    load_dotenv()
    account = os.environ['INSTAGRAM_ACCOUNT']
    password = os.environ['INSTAGRAM_PASSWORD']
    if SETTINGS.exists():
        api.load_settings(SETTINGS)
    api.login(account, password)
    try:
        api.get_timeline_feed()
    except LoginRequired:
        # delete current settings and restart
        SETTINGS.unlink()
        return create_logged_in_client()
    api.dump_settings(SETTINGS)
    return api


def pick_random_comment_from_url(api: Client, url: str) -> Comment:
    pk = api.media_pk_from_url(url)
    comments = api.media_comments(pk)
    return choice(comments)


def print_comment_info(comment: Comment) -> None:
    print(f'account: {comment.user.username}')
    print(f'name: {comment.user.full_name}')
    print(f'text: {comment.text}')


def main():
    url = sys.argv[1]
    api = create_logged_in_client()
    comment = pick_random_comment_from_url(api, url)
    print_comment_info(comment)


if __name__ == '__main__':
    main()
