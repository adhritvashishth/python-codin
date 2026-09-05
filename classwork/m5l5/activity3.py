class india():
    def capital(self):
        print("new delhi is capital of india")

    def language(self):
        print("hindi is the most spoken language of india")

    def type(self):
        print("india is a devloping country")

class USA():
    def capital(self):
        print("washinton D.C. is capital of USA")

    def language(self):
        print("english is the most spoken language of USA")

    def type(self):
        print("USA is a devloping country")
obj_india=india()
obj_USA=USA()


for i in(obj_india,obj_USA):
    i.capital()
    i.language()
    i.type()