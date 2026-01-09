names = ["Salman", "Nafila", "Asnif"]
ages = [18, 19, 17]

my_dict = [{name: age for name , age in zip(names, ages)}]

print(my_dict)