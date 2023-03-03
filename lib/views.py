from random import choice
from typing import Any

from aiohttp.web import Response, View
from aiohttp_jinja2 import render_template

from lib.instagram import get_comments_from_url


class IndexView(View):
    template = "index.html"

    async def get(self) -> Response:
        return render_template(self.template, self.request, {})

    async def post(self) -> Response:
        api = self.request.app["api"]
        ctx: dict[str, Any] = {}
        try:
            form = await self.request.post()
            url = str(form["url"])
            ctx["post_url"] = url
            comments = [
                {
                    "text": comment.text,
                    "username": comment.user.username,
                    "fullname": comment.user.full_name,
                    "winner": False,
                }
                for comment in get_comments_from_url(api, url)
            ]
            winner = choice(comments)
            winner["winner"] = True
            ctx["comments"] = comments
        except Exception as err:  # pylint: disable=broad-exception-caught
            ctx["error"] = str(err)
        return render_template(self.template, self.request, ctx)
