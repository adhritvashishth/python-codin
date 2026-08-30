class myclass:
    __privatevar=27
    def __privmeth(self):
        print("I am inside class my class")
    def hello(self):
        print(myclass.__privatevar)
foo=myclass()
print(foo.hello())
print(foo.__privmeth())