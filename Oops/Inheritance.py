class Animal:
    def sleep(self):
        print("Sleeping...")

class Dog(Animal):#Dog inherits from animal (from parent class)
    def bark(self):
        print("Bow Bow...")

d = Dog()
d.bark() #This is dog's
d.sleep() #This is from parent class


#This is an example Inheritance method