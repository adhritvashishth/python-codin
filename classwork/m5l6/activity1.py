class a:
    def __init__(self,a):
        self.a=a
    def __lt__(self, other):
        if self.a>other.a:
            return('object2 is lesser than object1')
        else:
            return('object1 is lesser that object2')
    def __eq__(self,other):
        if self.a==other.a:
            return("object1 and object2 are equal")
        else:
            return("object 1 and object2 are not equal")
obj1=a(2)
obj2=a(3)
print(obj1.a,obj2.a)
print(obj1<obj2)
obj3=a(4)
obj4=a(4)
print(obj3.a,obj4.a)
print(obj3==obj4)