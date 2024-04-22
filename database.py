from pymongo import MongoClient
from pymongo.collection import Collection

# Database configuration
DB_URL = "mongodb+srv://username:password@cluster-url/test?retryWrites=true&w=majority"  # Replace with your MongoDB Atlas URL
DB_NAME = "your_database_name"  # Replace with your database name

client = MongoClient(DB_URL)
db = client[DB_NAME]

def get_feed_items_collection() -> Collection:
    return db["feed_items"]

# Additional functions to manage database operations can be defined here
