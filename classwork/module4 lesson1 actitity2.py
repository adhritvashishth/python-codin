def match_word(list1):
    ctr=0
    lit=[]
    for i in list1:
       if len(i)>1 and i[0]==i[-1]:
           ctr=ctr+1
           lit.append(i)
    print('the list of words which have the same first and last words',lit) 
    return ctr
count=match_word(['asa','12221','92','apple'])
print(count)

