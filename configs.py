# (c) @PredatorHackerzZ || @TeleRoidGroup

import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "25826048"))
  API_HASH = os.environ.get("API_HASH", "b486ee260537697fdfc56b2b61cbc049")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "6882915473:AAGXS0a_EbgTwa03jQmYir8ZIqDhKPz1VDk")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "@file_storages_robot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002077818896"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "GreyMatterslinks.in")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "20eb8456008878c0349fc79d40fb4d1634cccf12")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "6324330202"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Bikash:Bikash@bikash.yl2nhcy.mongodb.net/?retryWrites=true&w=majority")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "https://t.me/deathshot_updates")
  LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1002126379861")
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [@PredatorHackerzZ](https://github.com/vikas-841)
 
 I am Super noob Please Support My Hard Work.

"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent FileStore Bot.

Join: @GreyMatter_Bots"""
