dog={}
dog={"Name":"Leite","Color":"White","Breed":"Fofinho","Legs":4,"Age":1}
student={"first_name":"Israel","last_name":"Jablonka","gender":"masculine","age":"25","marital status":True,"skills":"calm","country":"Israel","city":"Modiin","adress":"nachal tzin"}
print(len(student))
print(student["first_name"])
print(student.values())
student["age"]=26
print(student.keys())
print(student.items())
del student["age"]
del student