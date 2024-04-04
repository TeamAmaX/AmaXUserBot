import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from Anonymous import SUDO_USER
from Anonymous import app
from Anonymous.modules.help import add_help_cmd

@Client.on_message(filters.command(["spam"], ".") & (filters.me | filters.user(SUDO_USER)))
async def spam_handler(client: Client, message: Message):
        reply = message.reply_to_message
        reply_to_id = reply.id if reply else None
        cmd = message.text.split(None, 2)
        if not message.reply_to_message:
            await message.edit_text(
                "Reply or give me count & spam text after command.",
            )

        elif not reply and app.long() > 1:
            await message.delete()
            times = int(cmd[1]) if cmd[1].isdigit() else 0
            spam_msg = cmd[2]
            for _ in range(times):
                await client.send_message(
                    message.chat.id,
                    spam_msg,
                    reply_to_message_id=reply_to_id
                )
                await asyncio.sleep(0.10)

        elif reply:
            await message.delete()
            times = int(cmd[1]) if cmd[1].isdigit() else 0
            spam_msg = reply.id
            for _ in range(times):
                await client.copy_message(
                    message.chat.id,
                    message.chat.id,
                    spam_msg
                )



@Client.on_message(
    filters.command(["dspam", "delayspam"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def delayspam_handler(client: Client, message: Message):
        reply = message.reply_to_message
        cmd = message.command
        if len(message.command) < 3:
            await message.edit_text(
                f"Use like this: `.dspam [count spam] [delay time in seconds] [text messages]`"
            )

        elif len(message.command) > 2 and not reply:
            await message.delete()
            msg = message.text.split(None, 3)
            times = int(msg[1]) if msg[1].isdigit() else None
            sec = int(msg[2]) if msg[2].isdigit() else None
            text = msg[3]
            for _ in range(times):
                await client.send_message(
                    message.chat.id,
                    text
                )
                await asyncio.sleep(sec)
        else:
            await message.edit_text("Something wrong in spam command !")

add_help_cmd(
    "spam",
    [
        [
            ".spam [count]",
            "Reply to message/sticker and define count of spam.",
        ]
    ],
)
