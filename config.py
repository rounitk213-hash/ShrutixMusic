import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

def get_int_env(var_name, default):
    """Read int safely even if blank."""
    val = getenv(var_name)
    if not val or not val.isdigit():
        return int(default)
    return int(val)

# Telegram API
API_ID = get_int_env("API_ID", 22091901)
API_HASH = getenv("API_HASH", "54b0cd5fb47a40265b197f1a110b20b8")

# Bot Token
BOT_TOKEN = getenv("BOT_TOKEN", "8032338023:AAHvF1meONrnbAgMkkMTXQuxqVCu7PomcVU")

# MongoDB
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://bsdk:betichod@cluster0.fgj1r9z.mongodb.net/?retryWrites=true&w=majority")

# Limits
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))
LOGGER_ID = get_int_env("LOGGER_ID", -1003189576237)
OWNER_ID = get_int_env("OWNER_ID", 5811783004)

# Heroku
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

# Repo
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/NoxxOP/ShrutixMusic")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)

# Support
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/shadowmonarchjii")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+md2s35B2X1wxN2M9")

# Spotify
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

# Misc
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False").lower() == "true"
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))

# String Sessions
STRING1 = getenv("STRING_SESSION", "BQHtwy4AGGA4MHPmIjqksdceV3VZ9geDXnFRldvgPR1rbzrtiO2vuI7BYPV4GFSpIzeXmP86w9UVvJUQ7PtbSZofHnFzh_Jnc9YQtr7IDqkjNEXTSN6XkVn7aUAjpdFbIlZrHXwoVrVevopapdle_e134Ug-AhtzfwvmKkFb6cZ9tGuudsmLf2c6uBG-e1PkGKebj7biojgj5JTZ2bSGbKw9R1Td0lTFXGbJqomsmAtCKS_-iM900Q6r1RaNyY8IKv_lr8I7KUSSlmK-sLqXZHyGbyja6ezSUxGvLPzAdp6zg17Lsyft4a4R2f1FycaxjNUt5-_db8g5qcN3HXXpTm6efusOtwAAAAHwB2FsAA")
STRING2 = getenv("STRING_SESSION2", "BQGzDsUAZa04ZJqK2K2Lpsw8jKAsGzMdJEKxjpRjck3pQEY_UGWvSArZq0IZ8NiJNXifmSatXLT7I-RzPM-ADuyDqLeXb8CMAKgLO-cic1xWASnIKx2WlcnXahIq_7KebyGJwctj_uSoPyY_5qpv3ozxrIhNED8m5JL9rJc_4yk7n447Op-Ppqpqwb0oSGjfsfB2qC5ViYu6MDZco5adk4BdeL7Ze6wsXfJX-NwXDMvYEpQNzDr_fyFgdmPx6fHGW-D4XfhgHdiR-OWgR7FkZCRzCUXzm1PAs8IkLGF8ka6XP4N_kd2H3CiI47pGdccmSv9Nirb0nGh7eH1qDbDsIfvIeu0dlgAAAAHKFlg8AA")
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

# Default Data
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# Image URLs
START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/5c8d3994b93174a57d7f3-608459ffaf02cf2a9b.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://telegra.ph/file/c8b09659c837cd9142601-f594bfd29076e79944.jpg")
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# Validate links
if SUPPORT_CHANNEL and not re.match("(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - SUPPORT_CHANNEL must start with https://")
if SUPPORT_CHAT and not re.match("(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - SUPPORT_CHAT must start with https://")
