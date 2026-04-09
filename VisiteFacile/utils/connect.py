from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

bd = client["bd"]
visiteurs = bd["visiteurs"]


