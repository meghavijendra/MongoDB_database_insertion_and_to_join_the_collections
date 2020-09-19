# MongoDB_database_insertion_and_to_join_the_collections
This project has been developed using python and MongoDB query language

The input the program will be data files in flat relational format (text files in .csv format - comma separated values) for a COMPANY database 

The program will store this data in a collection in MongoDB in the following format:

 The PROJECTS document collection will store a collection of PROJECT documents. Each PROJECT document will include the following data about each PROJECT object (document): PNAME, PNUMBER, DNAME (for the controlling DEPARTMENT), and a collection of the workers (EMPLOYEES) who work on the project. This will be nested within the PROJECT object (document) and will include for each worker: EMP_LNAME, EMP_FNAME, HOURS.
 
 
The EMPLOYEES document collection will store a collection of EMPLOYEE documents. Each EMPLOYEE document will include the following data about each EMPLOYEE object (document): EMP_LNAME, EMP_FNAME, DNAME (department where the employee works), and a collection of the projects that the employee works on. This will be nested within the EMPLOYEE object (document) and will include for each project: PNAME, PNUMBER, HOURS.

This project has been developed using python and MongoDB query language. Steps to run the project are as follows:
1. First start the MongoDb server <br />
2. Install package pymongo. Run the Load_Data.py to load all the collections to the database <br />
3. Run Projects_Collection.py and Employees_Collection.py which will show the result of joining of the tables
in the nested format. The structure and the data in the newly created collection will be displayed on the terminal. <br />
4. install json2xml package. run json_to_xml.py to see the resulting JSON of the collections be displayed in the XML format on the terminal. <br />
5. Department_Collections.py which will show the result of joining of the tables
in the nested format. The structure and the data in the newly created collection will be displayed on the terminal.

