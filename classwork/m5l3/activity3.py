class bird:
    def __init__(self):
        print("bird is created")
    def whoisthis(self):
        print('bird')
    def swim(self):
        print("swim faster")
class penguin(bird):
    def __init__(self):
        super().__init__()
        print("penguin is ready")
    def whoisthis(self):
        print('penguin')
    def run(self):
        print("run faster")
penny=penguin()
penny.whoisthis()
penny.swim()
penny.run()