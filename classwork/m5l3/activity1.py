class vehical:
    def __init__(self,name,max_speed,milage):
        self.name=name
        self.max_speed=max_speed
        self.milage=milage
class bus(vehical):
    pass
school_bus=vehical("school volvo",180,12)
print(school_bus.name)
print(school_bus.max_speed)
print(school_bus.milage)