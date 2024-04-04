from datetime import datetime
from pyrogram.types import Message
from pyrogram import Client, filters
from Anonymous import app
from Anonymous import SUDO_USER
from Anonymous.modules.help import add_help_cmd

@Client.on_message(
    filters.command(["purge"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def purge(client: Client, message: Message):
    if message.reply_to_message:
        await message.edit_text("`Purging . . .`")
        start = datetime.now()
        messages = await client.get_messages(
            message.chat.id,
            range(message.reply_to_message.id, message.id),
            replies=0
        )

        msg_id = []
        msg_id.clear()

        for msg in messages:
            msg_id.append(msg.id)

        await client.delete_messages(
            message.chat.id,
            msg_id
        )

        sec = (datetime.now() - start).seconds

        await message.edit_text(
            "Deleted `{}` messages in `{}` seconds.".format(len(msg_id), sec),
        )
    else:
        await message.edit_text(
            "Reply to a message to delete all messages from tagged message to bottom message."
        )




@Client.on_message(filters.command(["purgeme", "pgm"], ".") & filters.me)
async def purgeme(client: Client, message: Message):
    if len(message.command) > 1:
        target = int(message.command[1]) if message.command[1].isdigit() and message.command[1] != 0 else 1
    else:
        return await message.edit_text(
            "Give me some number after command to delete messages."
        )
    start = datetime.now()
    lim = target + 1
    await message.edit_text(f"Deleting {target} messages . . .")
    msg_id = []
    msg_id.clear()
    async for msg in client.get_chat_history(message.chat.id, limit=lim):
        msg_id.append(msg.id)

    await client.delete_messages(message.chat.id, message_ids=msg_id[0:lim])
    sec = (datetime.now() - start).seconds

    await message.edit_text(
        "Deleted `{}` messages in `{}` seconds.".format(target, sec)
    )




@Client.on_message(filters.command(["del", "delme"], ".") & (filters.me | filters.user(SUDO_USER)))
async def delme(client: Client, message: Message):
    reply = message.reply_to_message
    msg_ids = [message.id, reply.id] if reply else [message.id]
    try:
        await client.delete_messages(message.chat.id, msg_ids)
    except Exception as e:
        await message.reply_text("`Something went wrong`")

add_command_help(
    "purge",
    [
        ["del", "to delete someone's message."],
        ["purge", "reply to all messages from your replied."],
        ["purgeme [count]", "to delete your messages only."],
        ["pgm [count]", "to delete your messages only."]
    ],
)
