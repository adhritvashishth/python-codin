s1={1,2,3,45,7}
s2={54,54,76,34,3}
a=zip(s1,s2)
s3=list(a)
print(s3)
l1=[2,4,6,8,35,6]
l2=[4,4,6,4,55,5]
for x,y in zip(l1,l2[::-1]):
    print(x,y)
list1=['reliance','tata moters']
list2=[765,5464]
new={a:b for a,b in zip(list1,list2)}
print(new)