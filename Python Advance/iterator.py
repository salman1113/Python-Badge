class CountToThree:
    def __iter__(self):
        self.num = 1
        return self
    
    def __next__(self):
        if self.num > 3:
            raise StopIteration
        
        value = self.num
        self.num += 1
        return value
    
for i in CountToThree():
    print(i)