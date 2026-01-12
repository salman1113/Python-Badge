n = 5

# for i in range(1, n+1):
#     print("*" * i)

# for i in range(n):
#     print("*" *n)

# for i in range(n, 0, -1):
#     print("*" * i)


#reversin a string 

# s = "Salman"
# reverse = ""

# i = len(s) - 1

# while i >= 0:
#     reverse += s[i]
#     i -= 1

# print(reverse)

# s = "salman"
# rev = ""

# for i in s:
#     rev = i + rev

# print(rev)



# n = 5
# fact = 1

# for i in range(1, n+1):
#     fact = fact * i

# print(fact)



# Remove duplicates from a list.

lst = [1, 2, 2, 3, 4, 5, 5, 6, 2]
# unique = []

# for x in lst:
#     if x not in unique:
#         unique.append(x)

# print(unique)

# unique = list(set(lst))
# print(unique)


# Find the second largest number in a list.

lst = [100, 200, 50, 100, 10]

lst = list(set(lst))
lst.sort()

print(lst[-2])

