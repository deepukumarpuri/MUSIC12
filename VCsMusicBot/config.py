import os
from os import path
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "tgbotproject")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/cf19dda907391656338eb.png")
admins = {}
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "VCsMusicPlayer")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "zauteschat")
PROJECT_NAME = getenv("PROJECT_NAME", "VCsMusicBot")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/ZauteKm/VCsMusicBot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "15"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
ADMINS = list(map(int, getenv("SUDO_USERS").split()))
LOG_CHANNEL = getenv("LOG_CHANNEL", None)
IMDB_TEMPLATE = getenv("IMDB_TEMPLATE", "VCsMusicBot")
DATABASE_URI = getenv("DATABASE_URI")
DATABASE_NAME = getenv("DATABASE_NAME", "Watermarks")
AUTH_CHANNEL = getenv("LOG_CHANNEL", None)
LONG_IMDB_DESCRIPTION = getenv("LONG_IMDB_DESCRIPTION", "VCsMusicBot")
MAX_LIST_ELM = getenv("MAX_LIST_ELM", None)
COLLECTION_NAME = getenv('COLLECTION_NAME', 'Telegram_files')
USE_CAPTION_FILTER = getenv('USE_CAPTION_FILTER', 'False')
