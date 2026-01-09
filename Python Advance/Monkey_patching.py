class Power:
    def square(self, num):
        return {num*num}
    
def monkey_patching(self, num): #Herer this is the monkey patching function.
    return {num*num*num}

Power.square = monkey_patching #Here we change the old function to new 

obj = Power()   
print(obj.square(2))