import re
from os import getenv

from dotenv import load_dotenv

load_dotenv()

##
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
STRING_SESSION = getenv("STRING_SESSION")
