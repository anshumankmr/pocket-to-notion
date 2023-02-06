import os
from dotenv import load_dotenv
load_dotenv()

config = {
    'notion_key' : os.environ.get('NOTION_KEY'),
    'notion_database': os.environ.get('NOTION_DATABASE_ID'),
    'debug': os.environ.get('DEBUG') or True,
    "access_token" :  os.environ.get('ACCESS_TOKEN'),
    "consumer_key" : os.environ.get('CONSUMER_KEY'),
}