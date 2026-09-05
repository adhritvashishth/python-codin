from abc import ABC,abstractmethod
class absclass(ABC):
    def print(self,x):
        print(x)
    @abstractmethod
    def task(self):
        print("we are in abs class")
        
class test_class(absclass):
    def task(self):
        print('we are inside test class')
test_obj=test_class()
test_obj.task()
test_obj.print(100)