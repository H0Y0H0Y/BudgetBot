from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_CONN_STRING = os.getenv("MONGODB_CONN_STRING")
DB = os.getenv("DB")
BOT_TOKEN = os.getenv("BOT_TOKEN")