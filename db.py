from pymongo import MongoClient


DB_NAME = "v-luminat"

DB_HOST = "mongodb+srv://ai_rn:TYwqhq9vVZ8qKh1G@cluster0-elnjz.mongodb.net/v-luminat?retryWrites=true&w=majority"
DB_PORT = ""
DB_USER = "ai_rn"
DB_PASS = "TYwqhq9vVZ8qKh1G"
 
connection = MongoClient(DB_HOST)
# db = connection.resumas
db = connection[DB_NAME]
# db.authenticate()