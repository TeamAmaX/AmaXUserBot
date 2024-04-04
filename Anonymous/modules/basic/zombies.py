import os
import asyncio
from pyrogram.types import Message
from pyrogram import Client, filters
from Anonymous import app, SUDO_USER
from Anonymous.modules.help import add_help_cmd


@Client.on_message(filters.command("zombies", ".") & filters.me)
async def zombies(client: Client, message: Message):
    temp_count = 0
    admin_count = 0
    count = 0

    if len(message.command) != 2:
        await message.edit_text("Checking deleted accounts . . .")

        async for x in client.get_chat_members(chat_id=message.chat.id):
            if x.user.is_deleted:
                temp_count += 1

        if temp_count > 0:
            await message.edit_text(f"**Found:** `{temp_count}` Deleted accounts\nUse `.zombies clean` to remove them from group.")
        else:
            await message.edit_text("No deleted accounts found.\nGroup is clean as Hell ! 😃")

    elif len(message.command) == 2 and message.command[1] == "clean":
        await message.edit_text("Cleaning deleted accounts . . .")

        async for x in client.get_chat_members(chat_id=message.chat.id):
            if x.user.is_deleted:
                if x.status in ("administrator", "creator"):
                    admin_count += 1
                    continue
                try:
                    await client.ban_chat_member(
                        chat_id=message.chat.id,
                        user_id=x.user.id
                    )
                    count += 1
                    await asyncio.sleep(0.2)
                except Exception as e:
                    return await message.edit_text(f"Something went wrong, please try again later ! Note : {e}")
        await app.send_edit(f"`Group clean up done !`\n\n**Total:** `{count+admin_count}`\n**Removed:** `{count}`\n**Not Removed:** `{admin_count}`\n\n**Note:** `Not removed accounts can be admins or the owner`")

    elif len(message.command) == 2 and message.command[1] != "clean":
        await  message.edit_text(f"Check `.help zombies` to see how it works !")
    else:
        await  message.edit_text("Something went wrong, please try again later !")

add_help_cmd(
    "zombies",
    [
        [".zombies", "to get deleted accounts count in chat."],
        [".zombies clean", "to clean deleted accounts from chat."]
    ],
)
