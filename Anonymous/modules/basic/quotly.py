import asyncio
from pyrogram.types import Message
from Anonymous import app, SUDO_USER
from pyrogram import Client, filters
from Anonymous.modules.help import add_help_cmd


@Client.on_message(filters.me & filters.command(["q", "quotly"], "."))
async def quotly(client: Client, message: Message):
        reply = message.reply_to_message
        if not reply:
            return await message.edit_text("Reply to any users text message")

        if len(message.command) > 1:
            color = message.text.split(None, 1)[1]
        else:
            color = "black"

        msg_one = await message.edit_text("Making a Quote . . .")
        await client.send_message("QuotLyBot", f"/qcolor {color}")
        await message.reply_to_message.forward("QuotLyBot")
        await asyncio.sleep(10)
        async for quotly in client.search_messages("QuotLyBot", limit=1):
            if quotly:
                await message.delete()
                await message.reply_sticker(
                    sticker=quotly.sticker.file_id,
                    reply_to_message_id=message.reply_to_message.id
                    if message.reply_to_message
                    else None,
                )
            else:
                return await message.edit("**Failed to Create Quotly Sticker**")

add_help_cmd(
    "quotly",
    [
        [
            f"q or .quotly",
            "To make an quote.",
        ],
        [
            f"q <color> or .quotly <color>",
            "Make a message into a sticker with the custom background color given.",
        ],
    ],
)
