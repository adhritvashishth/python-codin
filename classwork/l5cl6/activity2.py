class employee:
    def __init__(self):
        print("employee created")

    def __del__(self):
        print("destructor called")

def creat_obj():
    print("making object...")
    obj = employee()
    print('function ends...')
    return obj

print("calling creat_obj()function...")
obj=creat_obj()
print("program ends...")