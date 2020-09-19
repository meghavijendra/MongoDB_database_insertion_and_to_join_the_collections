from pymongo import MongoClient

try:
    client = MongoClient('mongodb://localhost:27017/')
    # Connected successfully!
except:
    print("Could not connect to MongoDB")

db = client.company


def loadData():
    #db.employee.remove({}) #If data already exists
    inpFile = open("data/EMPLOYEE.txt", 'r')
    for line in inpFile:
        line = line.rstrip('\n').replace("'", "")
        line = line.split(",")
        jsn = {
            "Fname": line[0].replace(" ", ""),
            "Minit": line[1].replace(" ", ""),
            "Lname": line[2].replace(" ", ""),
            "Ssn": line[3].replace(" ", ""),
            "Bdate": line[4].replace(" ", ""),
            "Address": line[5] + " " + line[6] + " " + line[7],
            "Sex": line[8].replace(" ", ""),
            "Salary": line[9].replace(" ", ""),
            "Super_ssn": line[10].replace(" ", ""),
            "Dno": line[11].replace(" ", "")
        }
        db.employee.insert_one(jsn)

    #db.department.remove({}) #If data already exists
    inpFile = open("data/DEPARTMENT.txt", 'r')
    for line in inpFile:
        line = line.rstrip('\n').replace("'","").replace(" ","")
        line = line.split(",")
        jsn = {
            "Dname": line[0],
            "Dnumber": line[1],
            "Mgr_ssn": line[2],
            "Mgr_start_date": line[3]
        }
        db.department.insert_one(jsn)

    #db.dept_locations.remove({}) #If data already exists
    inpFile = open("data/DEPT_LOCATIONS.txt", 'r')
    for line in inpFile:
        line = line.rstrip('\n').replace("'", "").replace(" ", "")
        line = line.split(",")
        jsn = {
            "Dnumber": line[0],
            "Dlocation": line[1]
        }
        db.dept_locations.insert_one(jsn)

    #db.project.remove({}) #If data already exists
    inpFile = open("data/PROJECT.txt", 'r')
    for line in inpFile:
        line = line.rstrip('\n').replace("'", "").replace(" ", "")
        line = line.split(",")
        jsn = {
            "Pname": line[0],
            "Pnumber": line[1],
            "Plocation": line[2],
            "Dnum": line[3]
        }
        db.project.insert_one(jsn)

    #db.works_on.remove({}) #If data already exists
    inpFile = open("data/WORKS_ON.txt", 'r')
    for line in inpFile:
        line = line.rstrip('\n').replace("'", "").replace(" ", "")
        line = line.split(",")
        jsn = {
            "Essn":line[0],
            "Pno": line[1],
            "Hours": line[2]
        }
        db.works_on.insert_one(jsn)

def main():
    loadData()

if __name__ == '__main__':
    main()