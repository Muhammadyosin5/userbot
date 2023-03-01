from pyrogram.client import Client
from pyrogram import filters
from pyrogram.types import Message
from dotenv import load_dotenv
import os
from pprint import pprint as print
from pyrogram.enums.parse_mode import ParseMode
load_dotenv()
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import parse_mode
api_id = os.getenv('api_id')
api_hash = os.getenv('api_hash')


app: Client = Client("sessions/my_account",str(api_id),str(api_hash))
