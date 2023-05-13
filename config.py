# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "25757134"))
API_HASH = os.environ.get("API_HASH", "4ab2cea7e4d196df9c850ac7f1c91c7f")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5959236310:AAGSD6oUi0qdZQ4HknQTfmfSA9QQQzw_SEI")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("5483441304")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Db Name")
DATABASE_URL = os.getenv("DATABASE_URL", "Monfo url") 
OWNER_ID =  int(os.environ.get("OWNER_ID", 5483441304")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(Id Owned Id)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "Logs Channels Id")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "Updates Channel User name Without @") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
