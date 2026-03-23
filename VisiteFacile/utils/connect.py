from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

bd = client["bd"]
<<<<<<< HEAD
visiteurs = bd["visiteurs"]
villes = bd["villes"]
#mongoimport --db bd --collection ville --file communes.json --jsonArray pour importer communes.json dans la bd
=======
visiteurs = bd["visiteurs"]
>>>>>>> 18a5dd302653e8cf24a5e0b869ed4aefeb86425d
