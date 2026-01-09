# def my_decorator(func):
#     def wrapper(a, b):
#         orginalsum = func(a, b)
#         final = orginalsum + 10
#         return final
#     return wrapper
    
# @my_decorator
# def add(c, d):
#     return c + d

# print(add(10, 80))

# This is an example of Decorator 

# def smart_divide(func):
#     def wrapper(a, b):
#         if b == 0:
#             return a
#         return func(a, b)
#     return wrapper

# @smart_divide
# def divide(a, b):
#     return a / b

# print(divide(10,2)) 
# print(divide(10,0))  



def math_calc(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return wrapper

@math_calc
def sum_calc(*args):
    return sum(args)

def soleve_equa(**kwargs):
    return kwargs['x'] + kwargs['y']

print(sum_calc(1,2,3,4,5))
print(soleve_equa(x=100, y=200))

#This is an example of decorator using ags and kwargs




