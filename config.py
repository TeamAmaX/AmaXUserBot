import re
from os import getenv

from dotenv import load_dotenv

load_dotenv()

##ISKE SATH NO BKC##

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
STRING_SESSION = getenv("STRING_SESSION")
STRING_SESSION2 = getenv("STRING_SESSION2")
STRING_SESSION3 = getenv("STRING_SESSION3")
STRING_SESSION4 = getenv("STRING_SESSION4")
STRING_SESSION5 = getenv("STRING_SESSION5")
MONGO_URL = getenv("MONGO_URL")
BOT_TOKEN = getenv("BOT_TOKEN")
LOG_GROUP = getenv("LOG_GROUP")
PM_LOGGER = getenv("PM_LOGGER")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
OWNER_ID = int(getenv("OWNER_ID"))
