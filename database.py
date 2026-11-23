from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://rebecamartinezg_db_user:6wx6G8VlMAjY5ccM@cluster0.zvd9rs0.mongodb.net/'
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["dbb_products_app"]
    except ConnectionError:
        print("Error de conexion con la bdd")
    return db