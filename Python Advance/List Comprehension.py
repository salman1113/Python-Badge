nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# my_list = []
# for n in nums:
#     my_list.append(n)

# print(my_list)

#This is the old way 


#example 1
# my_list = [n for n in nums]
# print(my_list)
#This is the new way which means list comprehension.


#example 2

# my_list = [n*n for n in nums]
# print(my_list)


#example 3
# my_list = [n for n in nums if n%2 == 0 ]
# print(my_list)


#example 4
# my_list = [(letters, num) for letters in 'abcd' for num in range(4)]
# print(my_list)