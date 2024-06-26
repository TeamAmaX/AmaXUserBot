from deep_translator import GoogleTranslator
from pyrogram.types import Message
from pyrogram import Client, filters

gtl = GoogleTranslator()


@Client.on_message(filters.command(["translate"], ".") & filters.me)
async def translate(client: Client, message: Message):
    reply = message.reply_to_message
    cmd = message.command
    oldmsg = message
    try:
        lang = cmd[1] if len(message.command) > 1 else "en"
        await message.edit_text(f"**Translating in** `{lang}` . . .")
        languages = list((gtl.get_supported_languages(as_dict=True)).values())
        if not lang in languages:
            return await message.edit_text("Bot doesn't support this language code, please try different one")
        if (reply and reply.text):
            tdata = await translate(lang=lang, text=reply.text)
            await message.edit_text(f"**Translated to:** `{lang}`\n\n**Text: **`{tdata}`")
        elif not reply and client.textlen(oldmsg) <= 4096:
            if len(message.command) <= 2:
                return await message.edit_text("Give me the language code with text to translate.")
            text = message.text.split(None, 2)[2]
            tdata = await translate(lang=lang, text=text)
            await message.edit_text(f"**Translated to:** `{lang}`\n\n**Text:** `{tdata}`")
        else:
            await message.edit_text("Something went wrong, please try again later !")
    except Exception as e:
        await message.edit_text("Something went wrong, please try again later !\n\n: {e}")


async def translate(lang, text):
    tr = GoogleTranslator(source="auto", target=lang)
    return tr.translate(text)

@Client.on_message(filters.command(["thelp","tlhelp"], ".") & filters.me)
async def translatehelp(client: Client, message: Message):
    data = []
    data.clear()
    langs_list = gtl.get_supported_languages(as_dict=True)  # output: {arabic: ar, french: fr, english: en etc.}
    for keys, values in zip(langs_list.values(), langs_list.keys()):
        data.append(f"`{keys}` : `{values}`")

    await message.edit_text("**SUPPORTED LANGUAGES:**\n\n" + "\n".join(data))
        
