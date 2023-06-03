import os
import logging
import logging.config

# Get logging configurations
logging.getLogger().setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram import Client
from pyromod import listen


API_ID = int(os.environ.get("API_ID", "12916125"))
API_HASH = os.environ.get("API_HASH", "dfebf9cc52b859771cf8a1d447e751a5")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6225708125:AAGf9b7YvJXmXCGjW1yF9KFZg3FzcqVd_1M")
API_KEY = os.environ.get("API_KEY", None)


def main():
    app = Client(name="String Session",
                 bot_token = BOT_TOKEN,
                 api_id = API_ID,
                 api_hash = API_HASH,
                 plugins = dict(root="plugins"),
                 workers = 100,
                 sleep_threshold = 15)

    app.run()


if __name__ == "__main__":
    main()
