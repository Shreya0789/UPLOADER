#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "20928172"))
API_HASH = environ.get("API_HASH", "48ed56c8db54f85d232f576b150360ef")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
OWNER = int(environ.get("OWNER", "6443740402"))
CHANNEL_ID = int(environ.get("CHANNEL_ID", "-1002850611486"))
CREDIT = "Shreya"
AUTH_USER = os.environ.get('AUTH_USERS', '6443740402').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
