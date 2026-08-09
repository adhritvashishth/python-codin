num1=[1,2,3,4,5]
num2=[6,7,8,9,10]
a=map(lambda x,y:x+y,num1,num2)
print("addtion of two lists")
print(list(a))
nums=[3,5,7,2]
def squar(n):
    return(n*n)
b=map(squar,nums)
print("squars of numbers in list")
print(list(b))