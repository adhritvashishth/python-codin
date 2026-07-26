studentdata={'id1':{'name':'krishiv','class':'7','subjectintegration':'maths, science,ssc'},
    'id2':{'name':'akash','class':'10','subjectintegration':'maths,science,ssc'} ,
    'id3':{'name':'arjun','class':'11','subjectintegration':'maths,science'},
    'id4':{'name':'arjuna','class':'10','subjectintegration':'maths,science,english'}}
result={}
seenkey=[]
for studentid, details in studentdata.items():
    uniquekey = (details['name'],details['class'],details['subjectintegration'])
    if uniquekey not in seenkey:
        seenkey.append(uniquekey)
        result[studentid]=details
for k,v in result.items():
    print(k,':',v)