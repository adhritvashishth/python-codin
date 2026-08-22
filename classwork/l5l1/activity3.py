class parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
blu=parrot('blu',10)
woo=parrot('woo',15)
print('woo is a ',woo.species)
print('blu is a ',blu.species)
print(blu.age,'is the age of blu',blu.name,'is the name of blu')
print(woo.age,'is the age of woo',woo.name,'is the name of woo')
