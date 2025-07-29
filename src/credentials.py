from dotenv import load_dotenv
import os

load_dotenv()

credentials = {
   "app_id": os.getenv('app_id'),
   "app_key": os.getenv('app_key')
}

print(credentials)
