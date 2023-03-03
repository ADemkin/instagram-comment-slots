import os
import sys

from dotenv import load_dotenv
from instagrapi.types import Comment

from lib.instagram import create_logged_in_client, pick_random_comment_from_url


def print_comment_info(comment: Comment) -> None:
    print(f"account: {comment.user.username}")
    print(f"name: {comment.user.full_name}")
    print(f"text: {comment.text}")


def main():
    url = sys.argv[1]
    load_dotenv()
    account = os.environ["INSTAGRAM_ACCOUNT"]
    password = os.environ["INSTAGRAM_PASSWORD"]
    api = create_logged_in_client(account, password)
    comment = pick_random_comment_from_url(api, url)
    print_comment_info(comment)


if __name__ == "__main__":
    main()
