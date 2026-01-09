from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def drive(self):
        pass #This is only the Design

class Tesla(Car):
    def drive(self):
        print("Driving Silently")

a = Tesla()
a.drive()


#This is an example of Abstraction method

        