import json
student = {}
student["name"]="Bartłomiej"
student["surname"]="Gręda"
student["age"]=27
student["fav"]=["chemia","matematyka"]
student["liceum"]=True
f = open("student.json","w")
json.dump(student,f,ensure_ascii=False)
