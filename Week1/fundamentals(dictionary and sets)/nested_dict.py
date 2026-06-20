student={
    "name":"shashank",
    "subjects": {
        "physics":77,
        "chemistry":85,
        "maths": 90
    }
}
print(student["subjects"]["chemistry"])#this gives error and using get() give none
print(list(student.keys()))
print(student.values())
print(student.items())
print(student.get("name")) #can have many functions inside each function
print(student.update({"college":"jbiet","age":16,"name":"arjun"}))

student["section"]= "c"
print(student)