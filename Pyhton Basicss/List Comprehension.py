# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
# square = []

# for n in nums:
#     if n % 2 == 0:
#         square.append(n*n)

# print(square)

#Here is a poblem that is more lines of code and, append() is calledd everytime.
#This problem is solved using List Comprehension.


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
squares = [n*n for n in nums if n % 2 == 0]
print(squares)

#Here the problem is solved using List Comprehension.
