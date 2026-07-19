def add_two(a,b):
    return(a+b)
def sub_two(a,b):
    return(a,b)
def mul_two(a,b):
    return(a*b)
def div_two("a/b"):
    return(a/b)
a=float(input("enter a number"))
b=float(input("enter a number"))
print("1 opption is addition,:2 opption is aubtraction,:3 opption is multiplication,:4 opption is divide")
opption=int(input("enter your opption"))
if opption ==1:
    add_two