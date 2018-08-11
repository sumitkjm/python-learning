students = {"Alice":["ID0001",26,"A"],
            "Bob":{"ID":"ID0002","Age":27,"Grade":"B"},
            "Claira":["ID0003",27,"C"],
            "Sumit":["ID0004",29,"D"],
            "Archana":["ID0005",30,"E"],
            "Sumit":["ID0006",36,"F"]}

print (students)

print (students["Sumit"])

del students["Sumit"]

print (students.keys())

list = list(students.keys())

print (list[1])

print (students.values())

print (students.items())

print (students["Archana"][0:])
print (students["Bob"]["Age"])
#print (students["Sumit"])