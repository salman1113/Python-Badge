#This is known as Anonymouse Functions.

#Normal Fucntion.

# def add (a, b):
#     return a + b

#Lamba Function

# add_lamda = lambda a , b : a + b


#Lamda With sort()

students = [
    {"name": "Salman", "age": 19},
    {"name": "Nafila", "age": 18},
    {"name": "Asnif", "age": 17}
]

sorted_students = sorted(students, key=lambda x: x["age"])
print(sorted_students)