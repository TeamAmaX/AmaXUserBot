from Anonymous import app
from pyrogram.types import Message
from pyrogram import filters, Client
from Anonymous.modules.help import add_help_cmd


@Client.on_message(filters.command(["react"], ".") & filters.me | filters.user(SUDO_USER))
async def gs(client: Client, message: Message):
 emoji = message.text.split(" ", 2)[2]
 await app.send_reaction(chat_id=message.chat.id, message_id=message.reply_to_message, emoji=emoji)

@Client.on_message(filters.command(["react"], ".") & filters.me | filters.user(SUDO_USER))
async def gs(client: Client, message: Message):
 emoji = message.text.split(" ", 2)[2]
 await app.send_reaction(chat_id=message.chat.id, message_id=message.reply_to_message, emoji=emoji)

@Client.on_message(filters.command(["send"], ".") & filters.me | filters.user(SUDO_USER))
async def gs(client: Client, message: Message):
 user_s_to_send = message.text.split(" ", 1)[1]
 emoji = message.text.split(" ", 2)[2]
 await app.send_reaction(chat_id=user_s_to_send, message_id=user_s_to_send, emoji=emoji)


add_help_cmd(
    "react/send",
    [
        [
            "reaction",
            "Get your private invite link. [Need Admin]",
        ],
        ["react : replyy to user message", "to invite someone."],
        ["send : mention chat id and message id with command"],
    ],
)
