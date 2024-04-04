import asyncio
from pyrogram import Client, filters, enums
from pyrogram.types import Message
from pyrogram.errors import PeerIdInvalid
from Anonymous import app, SUDO_USER
from Anonymous.modules.help import *

GROUP = [-1002060202794]
XO = GROUP
DEVS = [6154979500]
@Client.on_message(filters.command(["gcast"], ".") & (filters.me | filters.user(SUDO_USER)))
async def gcast(client: Client, message: Message):
    if message.reply_to_message or get_arg(message):
        tex = await message.reply_text("`Started global broadcast...`")
    else:
        return await message.edit_text("**Give A Message or Reply**")
    done = 0
    error = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            if message.reply_to_message:
                msg = message.reply_to_message
            elif get_arg:
                msg = get_arg(message)
            chat = dialog.chat.id
            if chat not in XO:
                try:
                    if message.reply_to_message:
                        await msg.copy(chat)
                    elif get_arg:
                        await client.send_message(chat, msg)
                    done += 1
                    await asyncio.sleep(0.3)
                except Exception:
                    error += 1
                    await asyncio.sleep(0.3)
    await tex.edit_text(
        f"**Successfully Sent Message To** `{done}` **Groups, chat, Failed to Send Message To** `{error}` **Groups**"
    )

add_help_cmd(
    "gcast",
    [
        [".gcast", "To global cast something !\n**Usage**:\n ```.gcast <reply/message>```"]
    ],
)
