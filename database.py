from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://edwardmancilla_db_user:A2fnGpVKLfkhSHJg@cluster0.nacd1nj.mongodb.net/'
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["dbb_products_app"]
    except ConnectionError:
        print("Error de conexion con la bdd")
    return db