import random
import importlib
import time
import asyncio
from pyrogram.types import Message
import config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, CallbackQuery
from Anonymous import app
from Anonymous.modules.help import add_help_cmd

CMD_HELP = {}

@Client.on_message(filters.command(["alive"], ".") & (filters.me))
async def start(client, message):
   X = await message.reply_text("**Starting...**")
   time.sleep(1.0)
   await client.edit_message_text(chat_id=message.chat.id, message_id=X.id, text="**Got it :\n\nJust a moment**")
   time.sleep(1.0)
   await client.edit_message_text(chat_id=message.chat.id, message_id=X.id, text="**TADDAAA :**\n\nIt's Your Own UserBot\n**#AnonymousUserBot**")

add_help_cmd(
    "alive",
    [
        [".alive", "Check if bot is alive"]
    ],
)