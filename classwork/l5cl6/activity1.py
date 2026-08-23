class IOString:
    def __init__(self):
        self.str1=""

    def get_string(self):
        self.str1=input("enter a string:")

    def print_string(self):
        print(self.str1.upper())

a=IOString()
a.get_string()
a.print_string()