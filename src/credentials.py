from dotenv import load_dotenv
import os

load_dotenv()

credentials = {
   "senha": os.getenv('senha'),
   "email": os.getenv('email'),
   "usuario": os.getenv('usuario')
}

print(credentials)
