from pymongo import MongoClient
from pprint import pprint

try:
    client = MongoClient('mongodb://localhost:27017/')
    # Connected successfully!
except:
    print("Could not connect to MongoDB")

db = client.company

dept_proj = db.project.aggregate([
   {
      "$lookup":
         {
           "from": "department",
           "let": {"number": "$Dnum"},
           "pipeline": [
              { "$match":
                 { "$expr":
                         { "$eq": [ "$Dnumber",  "$$number" ] }
                    }
                 }
              ],
           "as": "DP"
         },
    },
    {
      "$replaceRoot": { "newRoot": { "$mergeObjects": [ { "$arrayElemAt": [ "$DP", 0 ] }, "$$ROOT" ] } }
   },
    { "$project": { "_id": 0, "Pnumber": 1, "Pname": 1, "Dname":1 } }
])

works_employee = db.works_on.aggregate([
   {
      "$lookup":
         {
           "from": "employee",
           "let": {"ssn": "$Essn"},
           "pipeline": [
              { "$match":
                 { "$expr":
                         { "$eq": [ "$Ssn",  "$$ssn" ] }
                    }
                 }
              ],

           "as": "WE"
        },

     },
     {
      "$replaceRoot": { "newRoot": { "$mergeObjects": [ { "$arrayElemAt": [ "$WE", 0 ] }, "$$ROOT" ] } }
    },
    { "$project": { "_id":0, "Lname": 1, "Fname": 1, "Hours": 1, "Pno": 1} }
])

db.DP.insert_many(dept_proj)
db.WE.insert_many(works_employee)

PC = db.DP.aggregate([
   {
      "$lookup": {
         "from": "WE",
         "localField": "Pnumber",
         "foreignField": "Pno",
         "as": "Employees"
      }
   }
])

db.project_collection.insert_many(PC)
res = db.project_collection.find({},{"_id": 0, "Employees._id": 0})
for i in res:
    pprint(i)
