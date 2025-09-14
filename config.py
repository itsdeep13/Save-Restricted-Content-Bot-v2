# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "27473563"))
API_HASH = getenv("API_HASH", "bc2ea0765ac96bb474891b0243f44390")
BOT_TOKEN = getenv("BOT_TOKEN", "7085776844:AAE0YsI_5Jh8-H0yoDiyMd0HMXJwLKMfYRk")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6363345131,6478217960").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://uploaderbot:uploaderbot@cluster0.mpesxpw.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP = getenv("LOG_GROUP", "-1002879847444")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002983693521"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "1"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
