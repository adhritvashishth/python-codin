weather=(1,0,0,0,1,1,1)
sunny=0
rainy=0
for i in range(0,7):
    if weather[i]==1:
        sunny+=1
    elif weather[i]==0:
        rainy+=1
    else: 
        pass
if sunny>rainy:
    print("good weather")
else:
    print("bad weather")
