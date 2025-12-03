import os

class Config:
    API_ID = int(os.environ.get("API_ID", "0")) # Dari my.telegram.org
    API_HASH = os.environ.get("API_HASH", "")   # Dari my.telegram.org
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") # Dari BotFather
    # String Session buat Userbot (Ambil pake script generate session)
    SESSION_STRING = os.environ.get("SESSION_STRING", "") 
    OWNER_ID = int(os.environ.get("OWNER_ID", "0")) # ID Telegram Lu
