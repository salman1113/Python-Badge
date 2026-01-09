def add_items(my_list):
    my_list.append(100)

nums = [1, 2]
print(id(nums))
add_items(nums)
print(nums)
print(id(nums))


#This is an exaple of MUTABLE FUNCTION. 
#If you pass a mutable obeject to a function, the function can change the orginal data.

def add_number(num):
    return num + 100

val = 10
print(id(val))
val = add_number(val)
print(val)
print(id(val))

#This is an example of IMMUTABLE FUNCTION.
#if you pass a immutable object to a function, the function cannot change the orginal data.



#Immutable

a = 10
print(id(a))

a = a + 1
print(id(a))


#Mutable

lst = [1, 2]
print(id(lst))

lst.append(3)
print(id(lst))


my_tuple = (1, 2, ["A", "B"])
# my_tuple[1] = 5 #Error: Tuple object is immutable
# print(my_tuple)

my_tuple[2].append("C") # Here is this possible , bcz tuple is use the list memmory.
print(my_tuple)