from dotenv import load_dotenv
import os

load_dotenv()

credentials = {
   "accept": os.getenv("accept"),
   "app_id": os.getenv('app_id'),
   "app_key": os.getenv('app_key'),
   "ResourceVersion": os.getenv("ResourceVersion")
}


