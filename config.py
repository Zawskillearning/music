import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

#Get API_KEY from @LearningBotsOwner or @LearningBotsApiBot
API_BASE_URL = getenv("API_BASE_URL", "https://learningbots.site")
API_KEY = getenv("API_KEY")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1003563951808"))

# Get this value from @Harry_RoxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 6468293575))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "tg://user?id=6468293575",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/uchihahostgp")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/uchihahost")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "414df719f85e45c9bd0ee5e83d08b501")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "fa7e159a0b904b8b8505bf59b6458d3a")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv("START_IMG_URL", "https://image.zaw-myo.workers.dev/image/69756ba3-35e2-475a-934f-830bdbf73e97")
PING_IMG_URL = getenv("PING_IMG_URL", "https://image.zaw-myo.workers.dev/image/2c9c2a24-20d1-4ac7-ac01-a44ee34ffe83")
PLAYLIST_IMG_URL = "https://image.zaw-myo.workers.dev/image/24fc3c10-395f-4df8-99e2-2a373b171998"
STATS_IMG_URL = "https://image.zaw-myo.workers.dev/image/69756ba3-35e2-475a-934f-830bdbf73e97"
TELEGRAM_AUDIO_URL = "https://image.zaw-myo.workers.dev/image/2c9c2a24-20d1-4ac7-ac01-a44ee34ffe83"
TELEGRAM_VIDEO_URL = "https://image.zaw-myo.workers.dev/image/55f2147e-931e-4349-a714-907cc1d7be64"
STREAM_IMG_URL = "https://image.zaw-myo.workers.dev/image/32a96366-b1c0-4371-a305-5a893045e358"
SOUNCLOUD_IMG_URL = "https://image.zaw-myo.workers.dev/image/c249772d-541f-400e-a9a9-69b41fd8fddb"
YOUTUBE_IMG_URL = "https://image.zaw-myo.workers.dev/image/2c9c2a24-20d1-4ac7-ac01-a44ee34ffe83"
SPOTIFY_ARTIST_IMG_URL = "https://image.zaw-myo.workers.dev/image/32a96366-b1c0-4371-a305-5a893045e358"
SPOTIFY_ALBUM_IMG_URL = "https://image.zaw-myo.workers.dev/image/c249772d-541f-400e-a9a9-69b41fd8fddb"
SPOTIFY_PLAYLIST_IMG_URL = "https://image.zaw-myo.workers.dev/image/2c9c2a24-20d1-4ac7-ac01-a44ee34ffe83"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
