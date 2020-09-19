from pymongo import MongoClient
from pprint import pprint

try:
    client = MongoClient('mongodb://localhost:27017/')
    # Connected successfully!
except:
    print("Could not connect to MongoDB")

db = client.company

proj_works = db.works_on.aggregate([
    {
        "$lookup":
            {
                "from": "project",
                "let": {"number": "$Pno"},
                "pipeline": [
                    { "$match":
                        { "$expr":
                            { "$eq": ["$Pnumber", "$$number"]}
                        }
                    }
                ],
                "as": "PW"
            },
    },
    {
        "$replaceRoot": {"newRoot": {"$mergeObjects": [{"$arrayElemAt": ["$PW", 0]}, "$$ROOT"]}}
    },
    { "$project": {"_id": 0, "Pnumber": 1, "Pname": 1, "Hours": 1, "Essn": 1}}
])


employee_dept = db.employee.aggregate([
    {
        "$lookup":
            {
                "from": "department",
                "let": {"number": "$Dno"},
                "pipeline": [
                    { "$match":
                        { "$expr":
                            { "$eq": ["$Dnumber", "$$number"]}
                        }
                    }
                ],
                "as": "DE"
            },
    },
    {
        "$replaceRoot": {"newRoot": {"$mergeObjects": [{"$arrayElemAt": ["$DE", 0]}, "$$ROOT"]}}
    },
    { "$project": {"_id": 0, "Lname": 1, "Fname": 1, "Dname": 1, "Ssn": 1}}
])

db.PW.insert_many(proj_works)
db.DE.insert_many(employee_dept)

EC = db.DE.aggregate([
   {
      "$lookup": {
         "from": "PW",
         "localField": "Ssn",
         "foreignField": "Essn",
         "as": "Projects"
      }
   }
])

db.employee_collection.insert_many(EC)
res = db.employee_collection.find({},{"_id": 0, "Projects._id": 0})
for i in res:
    pprint(i)