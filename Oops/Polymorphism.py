class Sum:
    def calculate(self, a, b):
        return a + b
    
class Multiple:
    def calculate(self, a, b):
        return a * b 
    
result = [Sum(), Multiple()]

for maths in result:
    print(maths.calculate(10, 10)) #Here the function call is same , but the output is different for different classes

#This is an example of Polymorphism.