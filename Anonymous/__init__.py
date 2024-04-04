from pyrogram import Client
from config import API_ID, API_HASH, OWNER_ID, BOT_TOKEN, STRING_SESSION, STRING_SESSION2, STRING_SESSION3, STRING_SESSION4, STRING_SESSION5, SUDO_USERS
from datetime import datetime
import time
from aiohttp import ClientSession

StartTime = time.time()
START_TIME = datetime.now()
CMD_HELP = {}
clients = []
accounts = []
SUDO_USER = SUDO_USERS

app = Client(
    name="app",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Anonymous/modules/bot"),
    in_memory=True,
)

SUDO_USERS.append(OWNER_ID)
aiosession = ClientSession() 

if STRING_SESSION:
   client = Client(name="pyrocli", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION, plugins=dict(root="Anonymous/modules"))
   clients.append(client)

if STRING_SESSION2:
   client2 = Client(name="pyrocli2", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION2, plugins=dict(root="Anonymous/modules"))
   clients.append(client2)
    
if STRING_SESSION3:
   client3 = Client(name="pyrocli3", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION3, plugins=dict(root="Anonymous/modules"))
   clients.append(client3)
    
if STRING_SESSION4:
   client4 = Client(name="pyrocli4", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION4, plugins=dict(root="Anonymous/modules"))
   clients.append(client4)
    
if STRING_SESSION5:
   client5 = Client(name="pyrocli5", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION5, plugins=dict(root="Anonymous/modules"))
   clients.append(client5)
    
