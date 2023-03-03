from aiohttp.web import run_app
from dotenv import load_dotenv

from lib.app import create_app


def main() -> None:
    load_dotenv()
    app = create_app()
    run_app(app, host="0.0.0.0", port=7777)


if __name__ == "__main__":
    main()
