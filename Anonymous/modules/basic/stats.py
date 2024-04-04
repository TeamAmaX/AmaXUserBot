from pyrogram.types import Message
from pyrogram.enums import ChatType
from datetime import datetime
from pyrogram import Client, enums, filters
from pyrogram.types import Message
from Anonymous.modules.help import add_help_cmd

@Client.on_message(filters.command(["stats"], ".") & filters.me)
async def stats(client: Client, message: Message):
    X = await message.edit_text("`Collecting...`")
    start = datetime.now()
    u = 0
    g = 0
    sg = 0
    c = 0
    b = 0
    a_chat = 0
    Meh = await client.get_me()
    async for dialog in client.get_dialogs():
        if dialog.chat.type == enums.ChatType.PRIVATE:
            u += 1
        elif dialog.chat.type == enums.ChatType.BOT:
            b += 1
        elif dialog.chat.type == enums.ChatType.GROUP:
            g += 1
        elif dialog.chat.type == enums.ChatType.SUPERGROUP:
            sg += 1
            user_s = await dialog.chat.get_member(int(Meh.id))
            if user_s.status in (
                enums.ChatMemberStatus.OWNER,
                enums.ChatMemberStatus.ADMINISTRATOR,
            ):
                a_chat += 1
        elif dialog.chat.type == enums.ChatType.CHANNEL:
            c += 1

    end = datetime.now()
    ms = (end - start).seconds
    await X.edit_text(
        """**🔰 Stats for {} 🔰**\n
`Time Taken {} seconds`
⚡`Private Messages ➼ {}`
⚡`Private Groups ➼ {}`
⚡`Super Groups ➼ {}`
⚡`Channels ➼ {}`
⚡`Bots ➼ {}`
`You Are Admin in {} Chats.`\n
**Stats taken by [AmaX Userbot](https://github.com/AnoxDx/AnonymousUserBot)**""".format(client.me.mention(), ms, u, g, sg, c, b, a_chat), disable_web_page_preview=True)


add_help_cmd(
    "stats",
    [
        [".stats", "to get stats for your profile."]
    ],
)
