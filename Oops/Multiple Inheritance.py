# class Sum:
#     def sum(self, a, b):
#         return a + b        
    
# class Multiple:
#     def multipe(self, a, b):
#         return a * b

# class Calculator(Sum, Multiple):
#     pass

# c = Calculator()
# print(c.sum(2,3))
# print(c.multipe(3,2))



class A:
    def greet(self):
        print("This is grand father")

class B(A):
    def greet(self):
        super().greet()
        print("This is father")

class C(A):
    def greet(self):
        super().greet()
        print("This is Mother")

class D(B, C):
    def greet(self):
        super().greet()
        print("This is child")

d = D()
d.greet()
print(D.mro())


#This is an example of MRO and super().