from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

bd = client["bd"]
visiteurs = bd["visiteurs"]
villes = bd["villes"]
#mongoimport --db bd --collection ville --file communes.json --jsonArray pour importer communes.json dans la bd