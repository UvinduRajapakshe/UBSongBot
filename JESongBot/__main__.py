#nadunmalaka <https://t.me/NM_rider>

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from JESongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from JESongBot import Jebot as app
from JESongBot import LOGGER

pm_start_text = """
Hey [{}](tg://user?id={}), I'm Amdy Song Downloader Bot 🎵

😍 Just send me the song name you want to download.🎼🔊
      eg:```/song Faded```
      
A bot by @NM_rider 🇱🇰
"""

@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                     InlineKeyboardButton(
                        text="Support 🔊", url="https://t.me/Amdyx_bot"
                    ),
                    InlineKeyboardButton(
                        text="Dev 🔥", url="https://t.me/NM_rider"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)


app.start()
LOGGER.info("✅ NMSongBot is online.")
LOGGOR.info("🛠️ Bot created is sucsses ⚙️")
idle()
