from json2xml import json2xml
from json2xml.utils import readfromjson

print("Department collection XML: \n")
data = readfromjson("data/Dept_colldata.json")
print(json2xml.Json2xml(data,wrapper="Deptartments_collection", pretty=True).to_xml())

print("\n\nProject collection XML: \n")
data = readfromjson("data/Proj_colldata.json")
print(json2xml.Json2xml(data,wrapper="Projects_collection", pretty=True).to_xml())
#
print("\n\nEmployee collection XML: \n")
data = readfromjson("data/Emp_colldata.json")
print(json2xml.Json2xml(data,wrapper="Employees_collection", pretty=True).to_xml())

