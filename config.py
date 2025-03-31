import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7271765082:AAGjQifS0mQo0zh4p-9zPbrgQ8zeSAhKxPY")  # Ensure correct key name
    API_ID = int(os.environ.get("API_ID", "29520886"))  # Added key name and default value
    API_HASH = os.environ.get("API_HASH", "4e58d1ebff0c578501780e5032fb2f0d")  # Added key name for consistency

    AUTH_USER = os.environ.get("AUTH_USERS", "6886826162").split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]  # Ensuring list of integers

    HOST = os.environ.get("HOST", "https://api.masterapi.tech")  # Keeping HOST configurable
    CREDIT = os.environ.get("CREDIT", "𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎")  # Making CREDIT an environment variable for flexibility
