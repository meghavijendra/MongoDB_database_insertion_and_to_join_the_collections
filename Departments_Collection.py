from pymongo import MongoClient
from pprint import pprint

try:
    client = MongoClient('mongodb://localhost:27017/')
    # Connected successfully!
except:
    print("Could not connect to MongoDB")

db = client.company

dept_mgr = db.department.aggregate([
    {
        "$lookup":
            {
                "from": "employee",
                "let": {"ssn": "$Mgr_ssn"},
                "pipeline": [
                    { "$match":
                        { "$expr":
                            { "$eq": ["$Ssn", "$$ssn"]}
                        }
                    }
                ],
                "as": "WD"
            },
    },
    {
        "$replaceRoot": {"newRoot": {"$mergeObjects": [{"$arrayElemAt": ["$WD", 0]}, "$$ROOT"]}}
    },
    {"$project": {"_id": 0, "Lname": 1, "Fname": 1, "Dname": 1, "Ssn": 1}}
])

db.DM.insert_many(dept_mgr)

temp = db.employee.find({},{ "_id":0, "Fname": 1, "Lname": 1, "Salary": 1, "Super_ssn": 1})

db.tempo.insert_many(temp)

DC = db.DM.aggregate([
   {
      "$lookup": {
         "from": "tempo",
         "localField": "Ssn",
         "foreignField": "Super_ssn",
         "as": "workers"
      }
  }
])

db.department_collection.insert_many(DC)
res = db.department_collection.find({},{"_id": 0, "workers._id": 0})
for i in res:
    pprint(i)