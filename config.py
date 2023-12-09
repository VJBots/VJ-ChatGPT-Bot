import re
from os import getenv, environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

API_ID = int(environ.get("API_ID", "24942531"))
API_HASH = environ.get("API_HASH", "018f82cf994bd252038e9739fd68ba44")
BOT_TOKEN = environ.get("BOT_TOKEN", "6787109832:AAFQ2oCyxw3rk29gJfMyDIfTxXKIo78r5Ws")
OPENAI_API = environ.get("OPENAI_API", "")
AI = is_enabled((environ.get("AI","True")), False)
