from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("27013344"))
API_HASH = getenv("be5f160b65f07128459b4289c6e286ad")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("7062539103"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/70a9de40d206782967c72.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/b64a1fa450c5842fe5b47.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Riseeuniverse")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Riseeuniverse")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7062539103").split()))


FAILED = "https://telegra.ph/file/db864337b0db447e83784.jpg"
